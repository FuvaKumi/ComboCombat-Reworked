from gameloop import GameLoop
import pygame

class PvpGameLoop(GameLoop):
    def __init__(self):
        pass

    def run(self):
        pvp_running = True
        while pvp_running:
            # Event handling:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    pygame.quit()

                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pvp_running = False

            # PvP GameLoop funkciói:
            print('PvP GameLoop is running...')
            
