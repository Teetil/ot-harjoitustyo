import pygame
from services.main_loop import MainLoop

def main_menu(window):
    run = True
    game_over = 0
    while run:
        window.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 24)
        title = font.render("Press any key to start game", True, (255, 255, 255))
        window.blit(title, (window.get_width() // 2 - title.get_width() // 2, window.get_height() // 2 - title.get_height() // 2))
        for event in pygame.event.get():
            if event.type in (12, 256):
                run = False
            if event.type == pygame.KEYDOWN:
                ph_loop = MainLoop(window)
                game_over = ph_loop.loop()
        if game_over:
            lose_text = font.render("YOU LOSE!", True, (255, 0, 0))
            score_text = font.render(f"SCORE: {game_over}", True, (255, 0, 0))
            window.blit(lose_text, (window.get_width() // 2 - lose_text.get_width() // 2, window.get_height() // 4))
            window.blit(score_text, (window.get_width() // 2 - score_text.get_width() // 2, window.get_height() // 3))
        pygame.display.update()



    pygame.quit()