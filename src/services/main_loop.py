import pygame
from objects.player import Player
from ui.game_field import FieldRenderer
from services.stage import Stage
from repositories.score_handler import ScoreHandler


class MainLoop:
    """
    Luokka, joka pyörittää peliä
    """

    def __init__(self, window) -> None:
        """Luokan konstruktori, joka kutsutaan kun peli aloitetaan

        Args:
            window (pygame.surface): surface, jolle peli piirretään
        """
        self._clock = pygame.time.Clock()
        self._player = Player(window.get_width() // 2,
                              window.get_height() // 2, window)
        self._score_handler = ScoreHandler()
        self._renderer = FieldRenderer(window, self._score_handler)
        self._stage = Stage(window, self._player, self._score_handler)

    def loop(self) -> None:
        """Pelin sydän. Loop joka pahatuu 60 kertaa sekunissa ja hoitaa suuren osan live toiminnalisuudesta

        Returns:
            int: Funktio palauttaa pelaajan pisteet jos hän kuolee, jos peli exitataan muulla tavalla palautta None
        """
        while True:
            if not self._event_handler():
                return None
            self._player.movement(pygame.key.get_pressed())
            if not self._stage.update(self.get_time()):
                return self._score_handler.get_score()
            self._renderer.render_field(
                self._player, self._stage.enemies, self._stage.projectiles, self._stage._experience_gems)
            self._clock.tick(60)

    def _event_handler(self) -> bool:
        """Funktio hoitaa kaikki pelaajan tekemät asiat(eventit)

        Returns:
            bool: Funktio palauttaa False jos event on pygame.QUIT() ja sulkee main loopin
        """
        for event in pygame.event.get():
            if event.type in (12, 256):
                return False
            if event.type == 2:
                if event.dict["key"] == 27:
                    return False
        return True

    def get_time(self) -> int:
        return pygame.time.get_ticks()
