import pygame
from objects.player import Player
from ui.game_field import FieldRenderer

class MainLoop:
    """
    """

    def __init__(self, window):
        self._clock = pygame.time.Clock()
        self._player = Player(500, 500)
        self._renderer = FieldRenderer(window)

    def loop(self):
        while True:
            if self._event_handler() == False:
                break
            self._renderer.render_field(self._player)
            self._clock.tick(60)

    def _event_handler(self):
        for event in pygame.event.get():
            if event.type == 12:
                return False
