import pygame

class Player():

    def __init__(self, posX, posY) -> None:
        self._health = 100
        self._moveSpeed = 1
        self._damage = 1
        self.posX = posX
        self.posY = posY
