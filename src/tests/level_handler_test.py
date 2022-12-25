import unittest
from unittest.mock import Mock
from services.level_handler import LevelHandler

class TestLevelHandler(unittest.TestCase):
    def setUp(self) -> None:
        self.test_handler = LevelHandler()

    def test_should_level_works(self):
        first = self.test_handler.should_level()
        self.test_handler.experience += 1000
        second = self.test_handler.should_level()
        self.assertEqual(False, first)
        self.assertAlmostEqual(True, second)
