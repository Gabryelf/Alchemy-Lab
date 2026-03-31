"""The main class of the application"""

import pygame
from config import *
from player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.is_running = True

        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def draw(self):
         self.screen.fill((0, 0, 0))
         self.player.draw(self.screen)
         pygame.display.flip() 

    def update(self):
        # Получаем нажатые клавиши
        keys = pygame.key.get_pressed()
        self.player.move(keys)

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
    
