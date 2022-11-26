from objects.enemy import Enemy


class WaveHandler():
    def __init__(self, randomizer) -> None:
        self._waveDelay = 2000
        self.lastMove = 0
        self._waveCount = 5
        self._difficultyMod = 1
        self._randomizer = randomizer

    def spawnWave(self, fieldSize: int) -> list:
        spawned = []
        for n in range(self._waveCount):
            spawnX, spawnY = self._randomizer.randomSpawn(fieldSize, n)
            spawned.append(Enemy(spawnX, spawnY))
        return spawned

    def should_spawn(self, current_time: int) -> bool:
        return current_time - self.lastMove >= self._waveDelay
