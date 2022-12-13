import pygame


class FieldRenderer():
    """Luokka joka renderöi pelikentän
    """
    def __init__(self, window) -> None:
        """Luokan konstruktori

        Args:
            window (pygame.surface): alusta jolle pirtää pelikenttä
        """
        self.window = window
        self.font = pygame.font.SysFont(None, 24)

    def render_field(self, player, enemies: list, projectiles: list) -> None:
        """General funktio pelikentän piirtämiselle, joka kutsuu kaikki muut piirtofunktiot

        Args:
            player (playe): pelaaja, joka piirtää
            enemies (list): viholliset jotka piirtää
            projectiles (list): projectilet jotka pirtää
        """
        self.draw_window()
        self.draw_player(player)
        self.draw_enemy(enemies)
        self.draw_projectiles(projectiles)
        self.draw_text(player)
        pygame.display.update()

    def draw_window(self) -> None:
        self.window.fill((80, 80, 80))

    def draw_player(self, player) -> None:
        pygame.draw.rect(self.window, (0, 100, 0), player.rect)

    def draw_enemy(self, enemies: list) -> None:
        for enemy in enemies:
            pygame.draw.rect(self.window, (100, 0, 0), enemy.rect)

    def draw_projectiles(self, projectiles: list) -> None:
        for projectile in projectiles:
            pygame.draw.rect(self.window, (0, 0, 100), projectile.rect)

    def draw_text(self, player):
        """Pirtää tällä hetkellä pelaajan elämän ruudulle, myöhemmin myös muuta tekstiä

        Args:
            player (player): pelaaja, jonka elämä piirtää
        """
        health_text = self.font.render(str(player.health), True, (255, 0, 0))
        self.window.blit(health_text, (self.window.get_width() // 2, 50))
