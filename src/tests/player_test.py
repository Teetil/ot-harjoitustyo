import unittest
from objects.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(100, 100)
        self.test_key_list = [0] * 150

    def assert_coordinates_equal(self):
        player = Player(10, 10)
        self.assertEqual(player.pos_x, 10)
        self.assertEqual(player.pos_y, 10)

    def test_can_move_left(self):
        self.test_key_list[97] = 1
        self.player.movement(self.test_key_list)
        self.assertEqual(self.player.pos_x, 97)

    def test_can_move_right(self):
        self.test_key_list[100] = 1
        self.player.movement(self.test_key_list)
        self.assertEqual(self.player.pos_x, 103)

    def test_can_move_up(self):
        self.test_key_list[119] = 1
        self.player.movement(self.test_key_list)
        self.assertEqual(self.player.pos_y, 97)

    def test_can_move_down(self):
        self.test_key_list[115] = 1
        self.player.movement(self.test_key_list)
        self.assertEqual(self.player.pos_y, 103)
