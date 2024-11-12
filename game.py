import pygame
from main_menu import MainMenu
from pvp import PvpGameLoop
from settings_menu import SettingsMenu


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((300, 300))
        self.main_menu = MainMenu(self.screen)
        self.scenes = {
            'pvp': PvpGameLoop(self.screen),
            'settings': SettingsMenu(self.screen),
        }

    def run(self):
        pygame.init()
        self.screen.fill(pygame.color.THECOLORS['aliceblue'])
        pygame.display.flip()

        game_running = True
        while game_running:
            command = self.main_menu.run()
            self.scenes[command].run()

        pygame.quit()
