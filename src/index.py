import pygame
from services.main_loop import MainLoop

def main():
    window = pygame.display.set_mode((1000, 1000))
    phLoop = MainLoop(window)
    phLoop.loop()

if __name__ == "__main__":
    main()