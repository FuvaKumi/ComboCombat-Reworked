from gameloop import GameLoop
import pygame

class PvpGameLoop(GameLoop):
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

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
            self.screen.fill(pygame.color.THECOLORS['crimson'])
            self.screen.blit(pygame.font.Font(None, 32).render('PvP Game', True, (0, 0, 0)), (0, 0))
            pygame.display.update()
            
