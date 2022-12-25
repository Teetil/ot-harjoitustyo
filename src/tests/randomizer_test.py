import unittest
from services.randomizer import Random


class TestRandomizer(unittest.TestCase):
    def setUp(self) -> None:
        self.randomizer = Random()

    def test_should_spawn_works(self):
        self.assertLessEqual(20, self.randomizer.random_spawn(1000, 2)[0])
        self.assertGreaterEqual(990, self.randomizer.random_spawn(1000, 1)[0])
