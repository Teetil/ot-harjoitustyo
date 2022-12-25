import pygame


class Experience:
    def __init__(self, coords: tuple, difficulty_mod: int) -> None:
        self.value = 10 * difficulty_mod
        self.rect = pygame.Rect(coords, (10, 10))

    def update(self, player):
        if player.rect.colliderect(self.rect):
            return True
        return False
