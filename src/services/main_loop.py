import pygame
from objects.player import Player
from ui.game_field import FieldRenderer
from ui.level_menu import LevelMenu
from services.stage import Stage
from services.level_handler import LevelHandler
from repositories.score_handler import ScoreHandler


class MainLoop:
    """
    Luokka, joka pyörittää peliä
    """

    def __init__(self, window) -> None:
        """Luokan konstruktori

        Args:
            window (pygame.Surface): Taso jolle pelikenttä renderöidään
        """
        self._clock = pygame.time.Clock()
        self._player = Player(window.get_width() // 2,
                              window.get_height() // 2, window)
        self._score_handler = ScoreHandler()
        self._level_handler = LevelHandler()
        self._stage = Stage(window, self._player,
                            self._score_handler, self._level_handler)
        self._renderer = FieldRenderer(
            window, self._score_handler, self._level_handler)
        self._level_menu = LevelMenu(window, self._stage)

    def loop(self) -> None:
        """Pelin sydän. Loop joka pahatuu 60 kertaa sekunissa ja hoitaa suuren osan live toiminnalisuudesta
        Pelin normaali rendröinti ja muut toiminnot pysähtyy jos level_handler asettaa tauon päälle

        Returns:
            int: Funktio palauttaa pelaajan pisteet jos pelaaja kuolee, jos peli exitataan muulla tavalla palautta None
        """
        while True:
            if not self._event_handler():
                return None
            if not self._level_handler.paused:
                self._player.movement(pygame.key.get_pressed())
                if not self._stage.update(self.get_time()):
                    return self._score_handler.get_score()
                self._renderer.render_field(
                    self._player, self._stage.enemies, self._stage.projectiles, self._stage.experience_gems)
            else:
                if self._level_menu.level_up_menu():
                    self._level_handler.paused = False

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

    def _level_check(self):
        if self._level_handler.should_level():
            self._level_handler.level_up()

    def get_time(self) -> int:
        return pygame.time.get_ticks()
