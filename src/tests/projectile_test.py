import unittest
import pygame
from unittest.mock import Mock, MagicMock
from objects.projectile import Projectile
from objects.enemy import Enemy


class ProjectileTest(unittest.TestCase):
    def setUp(self) -> None:
        self.proj_attrs = {
            "damage": 10,
            "area": 10,
            "pierce": 1,
            "proj_speed": 3,
        }
        self.enemies = [Enemy(10, 10, 1)]
        self.test_projectile = Projectile(
            (10, 10), pygame.Vector2(15, 15), (0, 0, 0), self.proj_attrs)

    def test_move_works(self):
        self.test_projectile._move()
        self.assertEqual(
            (12, 12), (self.test_projectile.rect.x, self.test_projectile.rect.y))

    def test_normal_hit_works(self):
        self.test_projectile._hit(self.enemies)
        self.assertEqual(0, self.test_projectile._proj_attrs["pierce"])
        self.assertEqual(0, self.enemies[0].health)

    def test_explode_works(self):
        self.test_projectile._proj_attrs["explode"] = True
        self.test_projectile._explode()
        self.assertEqual(0.1, self.test_projectile._proj_attrs["proj_speed"])
        self.assertEqual(100, self.test_projectile._proj_attrs["pierce"])
        self.assertEqual(False, self.test_projectile._proj_attrs["explode"])
        self.assertEqual(30, self.test_projectile.rect.width)

    def test_pooling_works(self):
        self.test_projectile._proj_attrs["pool"] = True
        self.test_projectile._pool()
        self.assertEqual(0.1, self.test_projectile._proj_attrs["proj_speed"])
        self.assertEqual(10, self.test_projectile._proj_attrs["pierce"])
        self.assertEqual(False, self.test_projectile._proj_attrs["pool"])
        self.assertEqual(25, self.test_projectile.rect.width)

    def test_updating_works_default(self):
        self.test_projectile.update(self.enemies)
        self.assertEqual(12, self.test_projectile.rect.x)
        self.assertEqual(0, self.test_projectile._proj_attrs["pierce"])
