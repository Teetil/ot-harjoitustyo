import pygame


class Experience:
    """XP olion luokka
    """
    def __init__(self, coords: tuple, difficulty_mod: int) -> None:
        self.value = 10 * difficulty_mod
        self.rect = pygame.Rect(coords, (10, 10))

    def update(self, player):
        """Tarkistaa onko olio pelaajan sisällä

        Args:
            player (Player): Pelaaja, jonka hitbox tarkistaa

        Returns:
            bool: True jos osuu pelaajaan, False muuten
        """
        if player.rect.colliderect(self.rect):
            return True
        return False
