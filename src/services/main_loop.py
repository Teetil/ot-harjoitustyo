import pygame
from objects.player import Player
from ui.game_field import FieldRenderer
from services.stage import Stage


class MainLoop:
    """
    Luokka, joka pyörittää peliä
    """

    def __init__(self, window) -> None:
        self._clock = pygame.time.Clock()
        self._player = Player(500, 500)
        self._renderer = FieldRenderer(window)
        self._stage = Stage(window, self._player)

    def loop(self) -> None:
        while True:
            if not self._event_handler():
                break
            self._player.movement(pygame.key.get_pressed())
            self._stage.update(self.get_time())
            self._renderer.render_field(
                self._player, self._stage.enemies, self._stage.projectiles)
            self._clock.tick(60)

    def _event_handler(self) -> bool:
        for event in pygame.event.get():
            if event.type in (12, 256):
                return False
            if event.type == 2:
                if event.dict["key"] == 27:
                    return False
        return True

    def get_time(self) -> int:
        return pygame.time.get_ticks()
