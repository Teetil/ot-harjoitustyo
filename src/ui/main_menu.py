import pygame
from services.main_loop import MainLoop

def main_menu(window):
    run = True
    
    while run:
        window.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 24)
        title = font.render("Press any key to start game", True, (255, 255, 255))
        window.blit(title, (window.get_width() // 2, window.get_height() // 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type in (12, 256):
                run = False
            if event.type == pygame.KEYDOWN:
                ph_loop = MainLoop(window)
                ph_loop.loop()
    pygame.quit()