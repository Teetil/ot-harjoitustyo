import unittest
import pygame
from unittest.mock import Mock
from repositories.weapons import Weapon
from objects.player import Player
from objects.enemy import Enemy
from objects.projectile import Projectile


class TestWeapon(unittest.TestCase):
    def setUp(self) -> None:
        randomizer = Mock()
        randomizer.choice_list.side_effect = ["damage", "cooldown", "quantity"]
        self.test_weapon = Weapon({
            "damage": 1,
            "proj_speed": 1,
            "pierce": 1,
            "quantity": 1,
            "cooldown": 1,
            "area": 1
        }, randomizer, active=True)
        self.player = Player(
            100, 100, pygame.Surface((100, 100)))
        self.enemy = Enemy(100, 100, 1)

    def test_should_shoot_works(self):
        self.assertTrue(self.test_weapon.should_shoot(10))

    def test_get_nearest_works(self):
        res = self.test_weapon._get_nearest(self.player, [self.enemy])
        self.assertEqual(17, res[0].length())

    def test_shoot_nearest_works(self):
        res = self.test_weapon.shoot_nearest(self.player, [self.enemy])
        self.assertIsInstance(res[0], Projectile)

    def test_shoot_nearest_no_enemies_works(self):
        res = self.test_weapon.shoot_nearest(self.player, [])
        self.assertEqual([], res)

    def test_upgrade_random_works(self):
        self.test_weapon.upgrade_random()
        self.assertEqual(1.3, self.test_weapon.proj_attrs["damage"])
        self.test_weapon.upgrade_random()
        self.assertEqual(0.9, self.test_weapon._cooldown)
        self.test_weapon.upgrade_random()
        self.assertEqual(2, self.test_weapon._quantity)
