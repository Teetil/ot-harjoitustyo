from random import randint
from objects.enemy import Enemy

class WaveHandler():
    def __init__(self) -> None:
        self._waveDelay = 2000
        self.lastMove = 0
        self._waveCount = 5
        self._difficultyMod = 1
    
    def spawnWave(self, fieldSize : int) -> list:
        spawned = []
        for n in range(self._waveCount):
            spawnX, spawnY = self.randomSpawn(fieldSize, n)
            spawned.append(Enemy(spawnX, spawnY))
        return spawned

    def randomSpawn(self, fieldSize : int, directionMod : int) -> tuple:
        spawnY = randint(0, fieldSize)
        if directionMod % 2:
            spawnX = 0 + randint(1, 20)
        else:
            spawnX = fieldSize - 10 + randint(-20, 0)
        return spawnX, spawnY

    def should_spawn(self, current_time : int) -> bool:
        return current_time - self.lastMove >= self._waveDelay