class Enemy():
    def __init__(self, posX, posY, health = 10, damage = 1, moveSpeed = 2) -> None:
        self._health = health
        self._damage = damage
        self.posX = posX
        self.posY = posY