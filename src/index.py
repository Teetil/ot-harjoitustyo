import pygame
from ui.main_menu import main_menu



def main():
    pygame.init()
    window = pygame.display.set_mode((1000, 1000))
    main_menu(window)


if __name__ == "__main__":
    main()
