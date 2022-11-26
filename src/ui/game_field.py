import pygame

class FieldRenderer():

    def __init__(self, window) -> None:
        self.window = window

    def render_field(self, player):
        self.draw_window()
        self.draw_player(player)
        pygame.display.update()

    def draw_window(self):
        self.window.fill((80, 80, 80))
    
    def draw_player(self, player):
        pygame.draw.rect(self.window, (0, 100, 0), (player.posX, player.posY, 30, 60))