import pygame

class Player():

    def __init__(self, posX, posY) -> None:
        self._health = 100
        self.moveSpeed = 3
        self.damage = 1
        self.posX = posX
        self.posY = posY

    def movement(self, pressed_key):
        if pressed_key[97]:
            self.posX -= self.moveSpeed
        if pressed_key[100]:
            self.posX += self.moveSpeed
        if pressed_key[119]:
            self.posY -= self.moveSpeed
        if pressed_key[115]:
            self.posY += self.moveSpeed