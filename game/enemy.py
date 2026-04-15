# game/enemy.py
import pygame
import random


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 40
        self.color = (255, 0, 0)  # Красный
        self.speed = 2
        self.hp = 2

    def move_to_player(self, player_x, player_y):
        """Движется к игроку"""
        if self.x < player_x:
            self.x += self.speed
        elif self.x > player_x:
            self.x -= self.speed

        if self.y < player_y:
            self.y += self.speed
        elif self.y > player_y:
            self.y -= self.speed

    def hit(self):
        """Попадание по врагу"""
        self.hp -= 1
        return self.hp <= 0  # True если умер

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))