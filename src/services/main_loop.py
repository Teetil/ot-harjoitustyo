import pygame
from objects.player import Player
from ui.game_field import FieldRenderer
from services.stage import Stage

class MainLoop:
    """
    """

    def __init__(self, window) -> None:
        self._clock = pygame.time.Clock()
        self._player = Player(500, 500)
        self._renderer = FieldRenderer(window)
        self._stage = Stage(window)
        
    def loop(self) -> None:
        while True:
            if not self._event_handler():
                break
            self._player.movement(pygame.key.get_pressed())
            self._stage.update(self.get_time())
            self._renderer.render_field(self._player, self._stage.enemies)
            self._clock.tick(60)

    def _event_handler(self) -> bool:
        for event in pygame.event.get():
            if event.type == 12:
                return False
        return True

    def get_time(self) -> int:
        return pygame.time.get_ticks()