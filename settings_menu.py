import pygame

class SettingsMenu:
    def __init__(self):
        pass

    def run(self):
        settings_menu_running = True
        while settings_menu_running:
            # Event handling:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    pygame.quit()
                    settings_menu_running = False
                
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        settings_menu_running = False

            # Settings Menu funkciói:            
            print('Settings Menu is running...')