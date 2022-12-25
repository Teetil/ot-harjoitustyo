import pygame


class FieldRenderer():
    """Luokka joka renderöi pelikentän
    """

    def __init__(self, window: pygame.Surface, score_handler, level_handler) -> None:
        """Luokan konstruktori

        Args:
            window (pygame.Surface): alusta jolle pirtää pelikenttä
            score_handler: pistehallitsa pisteiden kirjoittamista näytölle varten
            level_handler: tason hallitsija XP palkin piirtämisen vuoksi
        """
        self.window = window
        self._score_handler = score_handler
        self._level_handler = level_handler
        self.font = pygame.font.SysFont(None, 24)

    def render_field(self, player, enemies: list, projectiles: list, experience_gems: list) -> None:
        """General funktio pelikentän piirtämiselle, joka kutsuu kaikki muut piirtofunktiot

        Args:
            player (playe): pelaaja, joka piirtää
            enemies (list): viholliset jotka piirtää
            projectiles (list): projectilet jotka pirtää
            experience_gems (lista): XP oliot jotka piirtää
        """
        self._draw_window()
        self._draw_projectiles(projectiles)
        self._draw_player(player)
        self._draw_enemy(enemies)
        self._draw_experience(experience_gems)
        self._draw_experience_bar()
        self._draw_text(player)
        pygame.display.update()

    def _draw_window(self) -> None:
        self.window.fill((80, 80, 80))

    def _draw_player(self, player) -> None:
        pygame.draw.rect(self.window, (0, 100, 0), player.rect)

    def _draw_enemy(self, enemies: list) -> None:
        for enemy in enemies:
            pygame.draw.rect(self.window, (100, 0, 0), enemy.rect)

    def _draw_projectiles(self, projectiles: list) -> None:
        for projectile in projectiles:
            pygame.draw.rect(self.window, projectile.color, projectile.rect)

    def _draw_experience(self, experience_gems: list) -> None:
        for experience in experience_gems:
            pygame.draw.rect(self.window, (0, 50, 100), experience.rect)

    def _draw_experience_bar(self):
        bar_heigth = self.window.get_height() - self.window.get_height() // 50
        bar_progress = self._level_handler.experience / \
            self._level_handler.experience_requirement * self.window.get_width()
        pygame.draw.line(self.window, (0, 50, 100), (0, bar_heigth),
                         (self.window.get_width(), bar_heigth))
        pygame.draw.rect(self.window, (0, 50, 100),
                         (0, bar_heigth, bar_progress, bar_heigth))

    def _draw_text(self, player):
        """Pirtää pelaajan elämän ja pisteet näytölle

        Args:
            player (player): pelaaja, jonka elämä piirtää
        """
        health_text = self.font.render(
            str(int(player.health)), True, (255, 0, 0))
        score_text = self.font.render(
            str(self._score_handler.get_score()), True, (0, 250, 0))
        self.window.blit(health_text, (self.window.get_width() //
                         2 - health_text.get_width() // 2, 150))
        self.window.blit(score_text, (self.window.get_width() //
                         2 - score_text.get_width() // 2, 50))
