import unittest
from unittest.mock import Mock
from objects.experience import Experience


class TestExperience(unittest.TestCase):

    def test_difficulty_scaling_works(self):
        new_experience = Experience((10, 10), 4)
        second_experience = Experience((10, 10), 10)
        self.assertEqual(40, new_experience.value)
        self.assertEqual(100, second_experience.value)

    def test_player_collision_works(self):
        player = Mock()
        player.rect.colliderect = Mock(side_effect=[True])
        exp = Experience((10, 10), 5)
        res = exp.update(player)
        self.assertEqual(True, res)

    def test_player_collision_no_hit(self):
        player = Mock()
        player.rect.colliderect = Mock(side_effect=[False])
        exp = Experience((10, 10), 5)
        res = exp.update(player)
        self.assertEqual(False, res)
