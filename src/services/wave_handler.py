from objects.enemy import Enemy


class WaveHandler():
    """Luokka joka hoitaa vihollisten luomisen
    """

    def __init__(self, randomizer,) -> None:
        """Konstruktori

        Args:
            randomizer (randomizer): Apu luokka testausta varten
        Attributes:
            wave_delay: Kuinka pitkään odottaa vihollisaaltojen välissä
            wave_count: kuinka monta vihollista luoda per wave
        """
        self._wave_delay = 2000
        self.last_move = 0
        self._wave_count = 5
        self._randomizer = randomizer

    def spawn_wave(self, field_size: int, difficulty: int) -> list:
        """Luokka joka luo viholliset kentän reunoille

        Args:
            field_size (int): Kentän koko

        Returns:
            list: lista luoduista vihollisista
        """
        spawned = []
        for dir_mod in range(self._wave_count):
            spawn_x, spawn_y = self._randomizer.random_spawn(
                field_size, dir_mod)
            spawned.append(Enemy(spawn_x, spawn_y, difficulty))
        return spawned

    def should_spawn(self, current_time: int, difficulty: int) -> bool:
        """Funktio joka tarikistaa pitäisikö luoda vihollisia

        Args:
            current_time (int): pelin nykyhetken aika

        Returns:
            bool: True jos pitäisi luoda vihollsia False muuten
        """
        return current_time - self.last_move >= self._wave_delay - difficulty * 75
