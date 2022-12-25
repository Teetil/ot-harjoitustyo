import unittest
from unittest.mock import Mock
import pygame
from objects.enemy import Enemy
from objects.player import Player


class TestEnemy(unittest.TestCase):
    def setUp(self) -> None:
        self.test_enemy = Enemy(10, 10, 1)
        self.player = Player(20, 20, pygame.Surface((100, 100)))

    def test_move_works(self):
        self.test_enemy._move(self.player)
        self.assertEqual(11, self.test_enemy.rect.x)

    def test_move_works_length_zero(self):
        self.player.rect.x = 10
        self.player.rect.y = 10
        self.test_enemy._move(self.player)
        self.assertEqual(10, self.test_enemy.rect.x)

    def test_dying_works(self):
        self.test_enemy.health = 10
        self.assertEqual(True, self.test_enemy.update(self.player))

    def difficulty_scaling_works(self):
        new_enemy = Enemy(10, 10, 5)
        self.assertEqual(50, new_enemy.health)
        self.assertEqual(2.8, new_enemy._move_speed)