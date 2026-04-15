# Полный код модификации со спрайтами и звуками

---

## game/game.py

### Добавление в Game __init__ шрифтов
```python
self.font = pygame.font.Font(None, 36)
self.big_font = pygame.font.Font(None, 72)
```

### Цвета в формате RGB
```python
RED = (255, 0, 0)
GREEN = (0, 255, 0)
```

### Добавление в Game draw текстов в самый конец метода перед `pygame.display.flip()`
```python
score_text = self.font.render(f"Score: {self.score}", True, WHITE)
self.screen.blit(score_text, (30, 22))

hp_text = self.font.render(f"HP: {self.player.hp}", True, RED)
self.screen.blit(hp_text, (170, 22))
```

### Изменение проверки на столкновение в методе update
```python
if player_rect.colliderect(enemy_rect):
    if self.player.is_alive():
        self.player.take_damage()
    else:
        self.state = STATE_MENU
```

---
## game/player.py

### Добавление в Player __init__ hp и спрайт
```python
self.hp = 100

self.image = None
self.load_image()
```

### Добавление в Player нового метода загрузки картинки
```python
    def load_image(self):
        self.image = pygame.image.load("assets/images/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
```

### Добавление в Player нового метода проверки на жизнь игрока
```python
    def is_alive(self):
        if self.hp <= 0:
            return False
        return True
```

### Добавление в Player нового метода нанесения урона по игроку
```python
    def take_damage(self):
        self.hp -= 1
```

### Изменить метод draw игрока
```python
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
```

---
## game/enemy.py

### Добавление в Enemy __init__ спрайт и показатель жизни
```python
self.max_hp = 2

self.image = None
self.load_image()
```

### Добавление в Enemy нового метода загрузки картинки
```python
    def load_image(self):
        self.image = pygame.image.load("assets/images/enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
```

### Изменить метод draw врага
```python
def draw(self, screen):
    screen.blit(self.image, (self.x, self.y))

    bar_width = self.size
    bar_height = 5
    health_percentage = self.hp / self.max_hp
    pygame.draw.rect(screen, RED,(self.x, self.y - 10, bar_width, bar_height))
    pygame.draw.rect(screen, GREEN,(self.x, self.y - 10, bar_width * health_percentage, bar_height))
```

## game/weapon.py

### Добавление в Weapon __init__ спрайт
```python
self.image = None
self.original_image = None
self.load_image()
```

### Добавление в Weapon метод подгрузки картинки
```python
   def load_image(self):
        self.original_image = pygame.image.load("assets/images/gun.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (30, 20))
        self.image = self.original_image
```

### Изменить метод draw оружия
```python
    def draw(self, screen):
        rotated_rect = self.image.get_rect(center=(self.x + 15, self.y + 10))
        screen.blit(self.image, rotated_rect)

        # Рисуем пули
        for bullet in self.bullets:
            bullet.draw(screen)
```

---

## utils/sound.py

### Создаем новый класс SoundManager
```python
"""Sound manager"""
import pygame


class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        self.load_sound('shoot', 'assets/sounds/shoot.mp3')
        try:
            pygame.mixer.music.load('assets/sounds/background.mp3')
            self.music_loaded = True
        except:
            self.music_loaded = False

    def load_sound(self, name, path):
        try:
            self.sounds[name] = pygame.mixer.Sound(path)
        except:
            self.sounds[name] = None

    def play(self, name):
        if name in self.sounds and self.sounds[name]:
            self.sounds[name].play()

    def play_music(self):
        if self.music_loaded:
            pygame.mixer.music.play()  # -1 = бесконечное повторение

    def stop_music(self):
        pygame.mixer.music.stop()

```

### Добавление в Weapon в метод shoot
```python
# Просто вызываем звук
if self.sound_manager:
    self.sound_manager.play('shoot')

```

### Добавление в Game __init__
```python
# Создаём звуковой менеджер
self.sound_manager = SoundManager()

# Включаем музыку
self.sound_manager.play_music()

```
