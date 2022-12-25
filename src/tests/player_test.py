import unittest
import pygame
from objects.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        window = pygame.Surface((1000, 1000))
        self.player = Player(100, 100, window)
        self.test_key_list = [0] * 150

    def assert_coordinates_equal(self):
        player = Player(10, 10)
        self.assertEqual(player.rect.x, 10)
        self.assertEqual(player.rect.y, 10)

    def test_can_move_left(self):
        self.test_key_list[97] = 1
        self.player.movement(self.test_key_list)
        self.assertEqual(self.player.rect.x, 96)

    def test_can_move_right(self):
        self.test_key_list[100] = 1
        self.player.movement(self.test_key_list)
        self.assertEqual(self.player.rect.x, 103)

    def test_can_move_up(self):
        self.test_key_list[119] = 1
        self.player.movement(self.test_key_list)
        self.assertEqual(self.player.rect.y, 96)

    def test_can_move_down(self):
        self.test_key_list[115] = 1
        self.player.movement(self.test_key_list)
        self.assertEqual(self.player.rect.y, 103)
