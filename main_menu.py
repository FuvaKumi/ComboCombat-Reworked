import pygame

class MainMenu:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def run(self):
        main_menu_running = True
        while main_menu_running:
            # Event handling:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    pygame.quit()
                    main_menu_running = False

                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_a:
                        return 'pvp'
                    elif e.key == pygame.K_b:
                        return 'settings'
                    elif e.key == pygame.K_ESCAPE:
                        pygame.quit()
                    
            # Main Menu funkciói:
            self.screen.fill(pygame.color.THECOLORS['cadetblue4'])
            self.screen.blit(pygame.font.Font(None, 32).render('Main Menu', True, (0, 0, 0)), (0, 0))
            pygame.display.update()
