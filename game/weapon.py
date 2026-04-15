class Weapon:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bullets = []
        self.shoot_cooldown = 0

    def update_position(self, x, y):
        """Следит за игроком"""
        self.x = x
        self.y = y

    def shoot(self, target_x, target_y):
        """Стреляет, если можно"""
        if self.shoot_cooldown <= 0:
            from game.bullet import Bullet
            self.bullets.append(Bullet(self.x, self.y, target_x, target_y))
            self.shoot_cooldown = 15  # Задержка в кадрах

    def update(self):
        """Обновляет пули"""
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        # Двигаем пули и удаляем улетевшие
        bullets_to_remove = []
        for i, bullet in enumerate(self.bullets):
            if bullet.move():
                bullets_to_remove.append(i)

        for i in reversed(bullets_to_remove):
            self.bullets.pop(i)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
