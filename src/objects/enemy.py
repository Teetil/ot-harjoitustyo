import pygame
class Enemy():
    def __init__(self, pos_x, pos_y, health=10, damage=1, move_speed=2) -> None:
        self._health = health
        self._damage = damage
        self._move_speed = move_speed
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self, player_x, player_y):
        dirvect = pygame.math.Vector2(player_x - self.pos_x, player_y - self.pos_y)
        dirvect.normalize()
        dirvect.scale_to_length(self._move_speed)
        self.pos_x += dirvect.x
        self.pos_y += dirvect.y
