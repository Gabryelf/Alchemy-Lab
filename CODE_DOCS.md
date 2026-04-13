# Полный код игры с описанием каждого метода

## Структура документа
1. [config/config.py - Настройки игры](#configconfigpy)
2. [game/player.py - Класс игрока](#gameplayerpy)
3. [game/enemy.py - Класс врага](#gameenemypy)
4. [game/bullet.py - Класс пули](#gamebulletpy)
5. [game/weapon.py - Класс оружия](#gameweaponpy)
6. [game/game.py - Главный класс игры](#gamegamepy)
7. [ui/panel.py - Базовая панель](#uipanelpy)
8. [ui/button.py - Кнопка](#uibuttonpy)
9. [ui/menu.py - Меню](#uimenupy)
10. [main.py - Точка входа](#mainpy)

---

## config/config.py

### Настройки экрана и FPS
```python
SCREEN_WIDTH = 800    # Ширина окна игры в пикселях
SCREEN_HEIGHT = 600   # Высота окна игры в пикселях
FPS = 60              # Максимальное количество кадров в секунду
```

### Цвета в формате RGB
```python
WHITE = (255, 255, 255)  # Белый цвет для текста
BLACK = (0, 0, 0)        # Черный цвет для фона
GRAY = (128, 128, 128)   # Серый цвет для панелей
BLUE = (0, 100, 255)     # Синий цвет для кнопок
```

### Состояния игры
```python
STATE_MENU = "menu"    # Игра в меню
STATE_GAME = "game"    # Игровой процесс
```

---

## game/player.py

### Метод `__init__(self, x, y)`
```python
def __init__(self, x, y):
    self.x = x                    # Координата X игрока
    self.y = y                    # Координата Y игрока
    self.width = 50               # Ширина игрока
    self.height = 50              # Высота игрока
    self.color = (0, 255, 0)      # Зеленый цвет
    self.speed = 5                # Скорость движения
```
**Описание:** Создает объект игрока в указанной позиции с заданными размерами и скоростью.

---

### Метод `move(self, keys)`
```python
def move(self, keys):
    # Движение влево с проверкой границы
    if keys[pygame.K_LEFT] and self.x > 0:
        self.x -= self.speed
    
    # Движение вправо с проверкой границы
    if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width:
        self.x += self.speed
    
    # Движение вверх с проверкой границы
    if keys[pygame.K_UP] and self.y > 0:
        self.y -= self.speed
    
    # Движение вниз с проверкой границы
    if keys[pygame.K_DOWN] and self.y < SCREEN_HEIGHT - self.height:
        self.y += self.speed
```
**Описание:** Обрабатывает нажатия клавиш стрелок и перемещает игрока, не позволяя выйти за границы экрана.

---

### Метод `draw(self, screen)`
```python
def draw(self, screen):
    # Рисует зеленый прямоугольник игрока
    pygame.draw.rect(screen, self.color, 
                    (self.x, self.y, self.width, self.height))
```
**Описание:** Отрисовывает игрока на экране в текущих координатах.

---

## game/enemy.py

### Метод `__init__(self, x, y)`
```python
def __init__(self, x, y):
    self.x = x                # Координата X врага
    self.y = y                # Координата Y врага
    self.size = 40            # Размер врага (квадрат)
    self.color = (255, 0, 0)  # Красный цвет
    self.speed = 2            # Скорость движения
    self.hp = 2               # Количество здоровья
```
**Описание:** Создает врага с заданными координатами, размером, скоростью и здоровьем.

---

### Метод `move_to_player(self, player_x, player_y)`
```python
def move_to_player(self, player_x, player_y):
    # Движение по горизонтали к игроку
    if self.x < player_x:
        self.x += self.speed    # Вправо
    elif self.x > player_x:
        self.x -= self.speed    # Влево
    
    # Движение по вертикали к игроку
    if self.y < player_y:
        self.y += self.speed    # Вниз
    elif self.y > player_y:
        self.y -= self.speed    # Вверх
```
**Описание:** Реализует простое движение врага по прямой линии к текущей позиции игрока.

---

### Метод `hit(self)`
```python
def hit(self):
    self.hp -= 1                # Уменьшаем здоровье на 1
    return self.hp <= 0         # Возвращаем True если враг мертв
```
**Описание:** Обрабатывает попадание по врагу и возвращает статус жизни.

---

### Метод `draw(self, screen)`
```python
def draw(self, screen):
    # Рисует красный квадрат врага
    pygame.draw.rect(screen, self.color, 
                    (int(self.x), int(self.y), self.size, self.size))
```
**Описание:** Отрисовывает врага на экране.

---

## game/bullet.py

### Метод `__init__(self, x, y, target_x, target_y)`
```python
def __init__(self, x, y, target_x, target_y):
    self.x = x                        # Начальная X пули
    self.y = y                        # Начальная Y пули
    self.size = 8                     # Размер пули
    self.color = (255, 255, 0)        # Желтый цвет
    self.speed = 10                   # Скорость пули
    
    # Вычисляем направление полета
    dx = target_x - x                 # Разница по X
    dy = target_y - y                 # Разница по Y
    
    # Вычисляем длину вектора
    length = (dx ** 2 + dy ** 2) ** 0.5
    
    # Нормализуем вектор и умножаем на скорость
    if length > 0:
        self.dx = (dx / length) * self.speed
        self.dy = (dy / length) * self.speed
    else:
        self.dx = 0
        self.dy = 0
```
**Описание:** Создает пулю и вычисляет вектор движения к точке клика мыши.

---

### Метод `move(self)`
```python
def move(self):
    # Перемещаем пулю
    self.x += self.dx
    self.y += self.dy
    
    # Проверяем выход за границы экрана
    if (self.x < -100 or self.x > 900 or 
        self.y < -100 or self.y > 700):
        return True     # Пуля улетела, нужно удалить
    return False        # Пуля еще в игре
```
**Описание:** Двигает пулю и проверяет, не улетела ли она за пределы экрана.

---

### Метод `draw(self, screen)`
```python
def draw(self, screen):
    # Рисует желтый квадрат пули
    pygame.draw.rect(screen, self.color, 
                    (int(self.x), int(self.y), self.size, self.size))
```
**Описание:** Отрисовывает пулю на экране.

---

## game/weapon.py

### Метод `__init__(self, x, y)`
```python
def __init__(self, x, y):
    self.x = x                    # Позиция оружия X
    self.y = y                    # Позиция оружия Y
    self.bullets = []             # Список активных пуль
    self.shoot_cooldown = 0       # Таймер перезарядки
```
**Описание:** Создает оружие в указанной позиции с пустым списком пуль.

---

### Метод `update_position(self, x, y)`
```python
def update_position(self, x, y):
    self.x = x      # Обновляем X
    self.y = y      # Обновляем Y
```
**Описание:** Обновляет позицию оружия (следует за игроком).

---

### Метод `shoot(self, target_x, target_y)`
```python
def shoot(self, target_x, target_y):
    # Проверяем, не на перезарядке ли оружие
    if self.shoot_cooldown <= 0:
        # Создаем новую пулю
        bullet = Bullet(self.x, self.y, target_x, target_y)
        self.bullets.append(bullet)      # Добавляем в список
        self.shoot_cooldown = 10         # Устанавливаем задержку
```
**Описание:** Создает новую пулю при клике мыши, если оружие готово к стрельбе.

---

### Метод `update(self)`
```python
def update(self):
    # Уменьшаем таймер перезарядки
    if self.shoot_cooldown > 0:
        self.shoot_cooldown -= 1
    
    # Список для удаления улетевших пуль
    bullets_to_remove = []
    
    # Проверяем каждую пулю
    for i, bullet in enumerate(self.bullets):
        if bullet.move():               # Если пуля улетела
            bullets_to_remove.append(i) # Запоминаем индекс
    
    # Удаляем пули в обратном порядке
    for i in reversed(bullets_to_remove):
        if i < len(self.bullets):
            self.bullets.pop(i)
```
**Описание:** Обновляет состояние оружия: перезарядку и все активные пули.

---

### Метод `draw(self, screen)`
```python
def draw(self, screen):
    # Рисуем все пули
    for bullet in self.bullets:
        bullet.draw(screen)
```
**Описание:** Отрисовывает все активные пули на экране.

---

## game/game.py

### Метод `__init__(self)`
```python
def __init__(self):
    # Инициализация Pygame
    pygame.init()
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    self.clock = pygame.time.Clock()
    self.is_running = True
    self.state = STATE_MENU
    self.font = pygame.font.Font(None, 36)
    
    # Игровые объекты
    self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    self.weapon = Weapon(self.player.x + 25, self.player.y + 25)
    self.enemies = []
    
    # Игровые переменные
    self.enemy_spawn_timer = 0
    self.score = 0
    
    # UI элементы
    self.top_panel = Panel(0, 0, SCREEN_WIDTH, 50, GRAY)
    menu_btn = Button(SCREEN_WIDTH - 100, 5, 90, 40, "MENU", BLUE, (100, 150, 255))
    self.top_panel.add_button(menu_btn)
    self.menu_panel = MenuPanel(SCREEN_WIDTH, SCREEN_HEIGHT)
```
**Описание:** Инициализирует игру, создает окно, объекты и UI.

---

### Метод `handle_events(self)`
```python
def handle_events(self):
    events = pygame.event.get()
    
    # Обработка всех событий
    for event in events:
        if event.type == pygame.QUIT:
            self.is_running = False
        
        # Стрельба в игре
        if self.state == STATE_GAME and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.weapon.shoot(mouse_x, mouse_y)
    
    # Обработка UI
    res = self.top_panel.handle_events(events)
    if res == "MENU":
        self.state = STATE_MENU
    
    if self.state == STATE_MENU:
        res = self.menu_panel.handle_events(events)
        if res == "START":
            self.reset_game()
            self.state = STATE_GAME
```
**Описание:** Обрабатывает все события ввода: закрытие окна, стрельбу, нажатие кнопок.

---

### Метод `reset_game(self)`
```python
def reset_game(self):
    # Создаем новых игрока и оружие
    self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    self.weapon = Weapon(self.player.x + 25, self.player.y + 25)
    
    # Очищаем список врагов
    self.enemies = []
    
    # Сбрасываем счет и таймеры
    self.score = 0
    self.enemy_spawn_timer = 0
```
**Описание:** Сбрасывает игру до начального состояния при нажатии START.

---

### Метод `spawn_enemy(self)`
```python
def spawn_enemy(self):
    # Выбираем случайную сторону экрана
    side = random.randint(0, 3)
    
    if side == 0:  # Левая сторона
        x = -50
        y = random.randint(0, SCREEN_HEIGHT)
    elif side == 1:  # Правая сторона
        x = SCREEN_WIDTH + 50
        y = random.randint(0, SCREEN_HEIGHT)
    elif side == 2:  # Верхняя сторона
        x = random.randint(0, SCREEN_WIDTH)
        y = -50
    else:  # Нижняя сторона
        x = random.randint(0, SCREEN_WIDTH)
        y = SCREEN_HEIGHT + 50
    
    # Создаем и добавляем врага
    enemy = Enemy(x, y)
    self.enemies.append(enemy)
```
**Описание:** Создает нового врага на случайном краю экрана.

---

### Метод `check_collisions(self)`
```python
def check_collisions(self):
    # Проверяем каждую пулю
    for bullet in self.weapon.bullets[:]:
        bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.size, bullet.size)
        
        # Проверяем каждого врага
        for enemy in self.enemies[:]:
            enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.size, enemy.size)
            
            # Если пуля попала во врага
            if bullet_rect.colliderect(enemy_rect):
                # Удаляем пулю
                if bullet in self.weapon.bullets:
                    self.weapon.bullets.remove(bullet)
                
                # Наносим урон врагу
                if enemy.hit():
                    if enemy in self.enemies:
                        self.enemies.remove(enemy)
                        self.score += 1
                break
```
**Описание:** Проверяет столкновения пуль с врагами и обрабатывает попадания.

---

### Метод `draw(self)`
```python
def draw(self):
    if self.state == STATE_MENU:
        # Рисуем меню
        self.menu_panel.draw(self.screen, self.font)
    else:
        # Рисуем игру
        self.screen.fill(BLACK)
        self.player.draw(self.screen)
        
        # Рисуем врагов
        for enemy in self.enemies:
            enemy.draw(self.screen)
        
        # Рисуем пули
        self.weapon.draw(self.screen)
        
        # Рисуем счет
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
    
    # Рисуем верхнюю панель
    self.top_panel.draw(self.screen, self.font)
    pygame.display.flip()
```
**Описание:** Отрисовывает все объекты в зависимости от состояния игры.

---

### Метод `update(self)`
```python
def update(self):
    if self.state == STATE_GAME:
        # Движение игрока
        keys = pygame.key.get_pressed()
        self.player.move(keys)
        
        # Обновляем оружие
        self.weapon.update_position(self.player.x + 25, self.player.y + 25)
        self.weapon.update()
        
        # Движение врагов
        player_center_x = self.player.x + 25
        player_center_y = self.player.y + 25
        
        for enemy in self.enemies:
            enemy.move_to_player(player_center_x, player_center_y)
        
        # Спавн врагов
        self.enemy_spawn_timer += 1
        if self.enemy_spawn_timer > 60:
            self.spawn_enemy()
            self.enemy_spawn_timer = 0
        
        # Проверка коллизий
        self.check_collisions()
        
        # Проверка столкновения игрока с врагом
        player_rect = pygame.Rect(self.player.x, self.player.y, 50, 50)
        for enemy in self.enemies:
            enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.size, enemy.size)
            if player_rect.colliderect(enemy_rect):
                self.state = STATE_MENU
```
**Описание:** Обновляет всю игровую логику каждый кадр.

---

### Метод `run(self)`
```python
def run(self):
    while self.is_running:
        self.handle_events()    # Обработка ввода
        self.update()           # Обновление логики
        self.draw()             # Отрисовка
        self.clock.tick(FPS)    # Ограничение FPS
```
**Описание:** Главный игровой цикл, который работает до закрытия игры.

---

## ui/panel.py

### Метод `__init__(self, x, y, width, height, color)`
```python
def __init__(self, x, y, width, height, color):
    self.rect = pygame.Rect(x, y, width, height)  # Прямоугольник панели
    self.color = color                             # Цвет панели
    self.buttons = []                              # Список кнопок
```
**Описание:** Создает панель с заданными координатами, размером и цветом.

---

### Метод `add_button(self, button)`
```python
def add_button(self, button):
    self.buttons.append(button)    # Добавляет кнопку в список
```
**Описание:** Добавляет кнопку на панель.

---

### Метод `handle_events(self, events)`
```python
def handle_events(self, events):
    for event in events:
        for button in self.buttons:
            if button.handle_event(event):    # Если кнопка нажата
                return button.text           # Возвращаем текст кнопки
    return None
```
**Описание:** Передает события всем кнопкам и возвращает текст нажатой.

---

### Метод `draw(self, screen, font)`
```python
def draw(self, screen, font):
    # Рисуем фон панели
    pygame.draw.rect(screen, self.color, self.rect)
    
    # Рисуем все кнопки
    for button in self.buttons:
        button.draw(screen, font)
```
**Описание:** Отрисовывает панель и все ее кнопки.

---

## ui/button.py

### Метод `__init__(self, x, y, width, height, text, color, hover_color)`
```python
def __init__(self, x, y, width, height, text, color, hover_color):
    self.rect = pygame.Rect(x, y, width, height)  # Прямоугольник кнопки
    self.text = text                               # Текст на кнопке
    self.color = color                             # Обычный цвет
    self.hover_color = hover_color                 # Цвет при наведении
    self.current_color = color                     # Текущий цвет
```
**Описание:** Создает кнопку с заданными параметрами и цветами.

---

### Метод `handle_event(self, event)`
```python
def handle_event(self, event):
    # Изменяем цвет при наведении мыши
    if event.type == pygame.MOUSEMOTION:
        if self.rect.collidepoint(event.pos):
            self.current_color = self.hover_color
        else:
            self.current_color = self.color
        return False
    
    # Проверяем нажатие
    if event.type == pygame.MOUSEBUTTONDOWN:
        if self.rect.collidepoint(event.pos):
            return True     # Кнопка нажата
    return False
```
**Описание:** Обрабатывает наведение и нажатие на кнопку.

---

### Метод `draw(self, screen, font)`
```python
def draw(self, screen, font=None):
    if font is None:
        font = pygame.font.Font(None, 36)
    
    # Рисуем фон кнопки
    pygame.draw.rect(screen, self.current_color, self.rect)
    
    # Рисуем рамку
    pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
    
    # Рисуем текст
    text_surf = font.render(self.text, True, (0, 0, 0))
    text_rect = text_surf.get_rect(center=self.rect.center)
    screen.blit(text_surf, text_rect)
```
**Описание:** Отрисовывает кнопку с текстом и рамкой.

---

## ui/menu.py

### Метод `__init__(self, screen_width, screen_height)`
```python
def __init__(self, screen_width, screen_height):
    # Создаем панель на весь экран
    super().__init__(0, 0, screen_width, screen_height, (50, 50, 50))
    
    # Вычисляем позицию кнопки по центру
    btn_width = 200
    btn_height = 50
    btn_x = screen_width // 2 - btn_width // 2
    btn_y = screen_height // 2 - btn_height // 2
    
    # Создаем кнопку START
    start_button = Button(btn_x, btn_y, btn_width, btn_height, 
                         "START", BLUE, (100, 150, 255))
    self.add_button(start_button)
```
**Описание:** Создает главное меню с кнопкой START по центру экрана.

---

## main.py

### Точка входа в программу
```python
if __name__ == "__main__":
    game = Game()        # Создаем объект игры
    game.run()           # Запускаем игровой цикл
    pygame.quit()        # Закрываем Pygame после выхода
```
**Описание:** Запускает игру при выполнении файла main.py.

---

## Схема взаимодействия методов

```
main.py
  └── Game.run()
       ├── Game.handle_events()
       │    ├── Weapon.shoot() → Bullet.__init__()
       │    └── MenuPanel.handle_events() → Button.handle_event()
       │
       ├── Game.update()
       │    ├── Player.move()
       │    ├── Weapon.update()
       │    │    └── Bullet.move()
       │    ├── Enemy.move_to_player()
       │    ├── Game.spawn_enemy()
       │    └── Game.check_collisions()
       │         └── Enemy.hit()
       │
       └── Game.draw()
            ├── Player.draw()
            ├── Enemy.draw()
            ├── Weapon.draw()
            │    └── Bullet.draw()
            └── Panel.draw()
                 └── Button.draw()
```

---

## Краткое описание всех методов (шпаргалка)

| Класс | Метод | Что делает |
|-------|-------|------------|
| **Game** | `__init__()` | Создает окно и все объекты |
| | `handle_events()` | Обрабатывает нажатия клавиш и мыши |
| | `reset_game()` | Сбрасывает игру в начальное состояние |
| | `spawn_enemy()` | Создает врага на краю экрана |
| | `check_collisions()` | Проверяет попадания пуль во врагов |
| | `draw()` | Рисует все объекты |
| | `update()` | Обновляет логику игры |
| | `run()` | Главный игровой цикл |
| **Player** | `__init__()` | Создает игрока |
| | `move()` | Двигает игрока по стрелкам |
| | `draw()` | Рисует игрока |
| **Enemy** | `__init__()` | Создает врага |
| | `move_to_player()` | Двигает врага к игроку |
| | `hit()` | Обрабатывает попадание |
| | `draw()` | Рисует врага |
| **Weapon** | `__init__()` | Создает оружие |
| | `update_position()` | Следит за игроком |
| | `shoot()` | Создает новую пулю |
| | `update()` | Обновляет пули |
| | `draw()` | Рисует все пули |
| **Bullet** | `__init__()` | Создает пулю с направлением |
| | `move()` | Двигает пулю |
| | `draw()` | Рисует пулю |
| **Panel** | `__init__()` | Создает панель |
| | `add_button()` | Добавляет кнопку |
| | `handle_events()` | Обрабатывает кнопки |
| | `draw()` | Рисует панель |
| **Button** | `__init__()` | Создает кнопку |
| | `handle_event()` | Обрабатывает нажатие |
| | `draw()` | Рисует кнопку |
| **MenuPanel** | `__init__()` | Создает меню с кнопкой START |

---
