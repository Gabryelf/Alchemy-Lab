"""The main class of the application"""

import pygame
from config.config import *
from game.player import Player
from ui.menu import MenuPanel
from ui.panel import Panel
from ui.button import Button


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.state = STATE_MENU
        self.font = pygame.font.Font(None, 36)

        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.top_panel = Panel(0, 0, SCREEN_WIDTH, 50, GRAY)
        menu_btn = Button(SCREEN_WIDTH - 100, 5, 90, 40, "MENU", BLUE, (100, 150, 255))
        self.top_panel.add_button(menu_btn)

        self.menu_panel = MenuPanel(SCREEN_WIDTH, SCREEN_HEIGHT)

    def handle_events(self):
        events = pygame.event.get()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

        res = self.top_panel.handle_events(events)
        if res == "MENU":
            self.state = STATE_MENU

        if self.state == STATE_MENU:
            res = self.menu_panel.handle_events(events)
            if res == "START":
                self.state = STATE_GAME

    def draw(self):
        if self.state == STATE_MENU:
            self.menu_panel.draw(self.screen, self.font)
        else:
            self.screen.fill(BLACK)
            self.player.draw(self.screen)

        self.top_panel.draw(self.screen, self.font)
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
    
