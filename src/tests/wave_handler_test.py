import unittest
from services.wave_handler import WaveHandler


class StubRandom():
    def __init__(self, ret_num: int) -> None:
        self.ret_num = ret_num

    def random_spawn(self, field_size, direction_mod):
        return self.ret_num, self.ret_num


class TestWaveHandler(unittest.TestCase):
    def setUp(self):
        self.wave_handler = WaveHandler(StubRandom(10))

    def test_spawn_count(self):
        self.assertEqual(len(self.wave_handler.spawn_wave(1000)), 5)
