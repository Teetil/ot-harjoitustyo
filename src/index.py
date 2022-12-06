import pygame
from services.main_loop import MainLoop


def main():
    pygame.init()
    window = pygame.display.set_mode((1000, 1000))
    ph_loop = MainLoop(window)
    ph_loop.loop()


if __name__ == "__main__":
    main()
