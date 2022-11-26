from objects.enemy import Enemy


class WaveHandler():
    def __init__(self, randomizer) -> None:
        self._wave_delay = 2000
        self.last_move = 0
        self._wave_count = 5
        self._difficulty_mod = 1
        self._randomizer = randomizer

    def spawn_wave(self, field_size: int) -> list:
        spawned = []
        for dir_mod in range(self._wave_count):
            spawn_x, spawn_y = self._randomizer.random_spawn(
                field_size, dir_mod)
            spawned.append(Enemy(spawn_x, spawn_y))
        return spawned

    def should_spawn(self, current_time: int) -> bool:
        return current_time - self.last_move >= self._wave_delay
