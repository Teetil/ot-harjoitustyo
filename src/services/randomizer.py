from random import randint

class Random():
    def randomSpawn(self, fieldSize : int, directionMod : int) -> tuple:
        spawnY = randint(0, fieldSize)
        if directionMod % 2:
            spawnX = 0 + randint(1, 20)
        else:
            spawnX = fieldSize - 10 + randint(-20, 0)
        return spawnX, spawnY