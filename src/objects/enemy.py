import pygame


class Enemy():
    def __init__(self, pos_x, pos_y, health=10, damage=1, move_speed=2) -> None:
        self._health = health
        self._damage = damage
        self._move_speed = move_speed
        self.rect = pygame.Rect(pos_x, pos_y, 15, 15)

    def update(self, player):
        self.move(player)
        self.damage(player)
        if self.health <= 0:
            return True
        return False

    def move(self, player) -> None:
        dirvect = pygame.math.Vector2(
            player.rect.centerx - self.rect.centerx, player.rect.centery - self.rect.centery)
        if dirvect.length() == 0:
            return False
        dirvect.normalize()
        dirvect.scale_to_length(self._move_speed)
        self.rect.move_ip(dirvect)
        return True

    def damage(self, player):
        if self.rect.colliderect(player.rect):
            player.health = self._damage

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, damage):
        self._health -= damage
