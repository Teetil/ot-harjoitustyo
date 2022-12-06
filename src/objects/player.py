import pygame


class Player():

    def __init__(self, pos_x: int, pos_y: int, health=100, move_speed=3, damage=1) -> None:
        self._health = health
        self.move_speed = move_speed
        self.damage = damage
        self.rect = pygame.Rect(pos_x, pos_y, 30, 60)

    def movement(self, pressed_key: list):
        if pressed_key[97]:
            self.rect.x -= self.move_speed
        if pressed_key[100]:
            self.rect.x += self.move_speed
        if pressed_key[119]:
            self.rect.y -= self.move_speed
        if pressed_key[115]:
            self.rect.y += self.move_speed

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, damage):
        self._health -= damage
        if self._health <= 0:
            pass
