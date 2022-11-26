class Player():

    def __init__(self, posX : int, posY : int, health=100, movespeed=3, damage=1) -> None:
        self._health = health
        self.moveSpeed = movespeed
        self.damage = damage
        self.posX = posX
        self.posY = posY

    def movement(self, pressed_key : list):
        if pressed_key[97]:
            self.posX -= self.moveSpeed
        if pressed_key[100]:
            self.posX += self.moveSpeed
        if pressed_key[119]:
            self.posY -= self.moveSpeed
        if pressed_key[115]:
            self.posY += self.moveSpeed