import pygame

class Projectile:
    def __init__(self, pos_x : int, pos_y : int, vector : pygame.Vector2, damage : int, pierce : int, proj_speed, area : int) -> None:
        self.rect = pygame.Rect(pos_x, pos_y, area, area)
        self._vector = vector
        self._damage = damage
        self._pierce = pierce
        self._proj_speed = proj_speed
        self._hitlist = []
    
    def update(self, enemies):
        self.move()
        self.hit(enemies)
        if self._pierce == 0:
            return True

    def move(self):
        self._vector.normalize()
        self._vector.scale_to_length(self._proj_speed)
        self.rect.move_ip(self._vector)

    def hit(self, enemies):
        collidelist = self.rect.collidelistall(enemies)
        for index in collidelist:
            if self._pierce > 0:
                self._pierce -= 1
                enemies[index].health = self._damage
    
