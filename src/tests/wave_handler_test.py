import unittest
from services.wave_handler import WaveHandler


class StubRandom():
    def __init__(self, retNum: int) -> None:
        self.retNum = retNum

    def randomSpawn(self, fieldSize, directionMod):
        return self.retNum, self.retNum


class TestWaveHandler(unittest.TestCase):
    def setUp(self):
        self.waveHandler = WaveHandler(StubRandom(10))

    def test_spawn_count(self):
        self.assertEqual(len(self.waveHandler.spawnWave(1000)), 5)
