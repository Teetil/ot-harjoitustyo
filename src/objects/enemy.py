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

    def move(self, player) -> None:
        dirvect = pygame.math.Vector2(player.rect.x- self.rect.x, player.rect.y - self.rect.y)
        if dirvect.length() == 0:
            return False
        dirvect.normalize()
        dirvect.scale_to_length(self._move_speed)
        self.rect.move_ip(dirvect)
        return True
    
    def damage(self, player):
        if self.rect.colliderect(player.rect):
            player.health =  self._damage