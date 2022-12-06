import pygame
class Enemy():
    def __init__(self, pos_x, pos_y, health=10, damage=1, move_speed=2) -> None:
        self._health = health
        self._damage = damage
        self._move_speed = move_speed
        self.rect = pygame.Rect(pos_x, pos_y, 15, 15)

    def move(self, player) -> None:
        dirvect = pygame.math.Vector2(player.rect.x- self.rect.x, player.rect.y - self.rect.y)
        dirvect.normalize()
        dirvect.scale_to_length(self._move_speed)
        self.rect.move_ip(dirvect)
    
    def damage(self, player):
        pass