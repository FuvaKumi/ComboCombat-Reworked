import pygame
from main_menu import MainMenu
from pvp import PvpGameLoop


class Game:
    def __init__(self):
        self.main_menu = MainMenu()
        self.game_loops = {
            'pvp': PvpGameLoop(),
        }

    def run(self):
        pygame.init()

        command = self.main_menu.run()

        self.game_loops[command].run()
