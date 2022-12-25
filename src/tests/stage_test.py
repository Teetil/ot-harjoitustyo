import unittest
import pygame
from unittest.mock import Mock
from services.stage import Stage
from objects.player import Player


class TestStage(unittest.TestCase):
    def setUp(self):
        self.window = pygame.Surface((100, 100))
        self.player = Mock(wraps=Player(10, 10, self.window))
        self.score_handler = Mock()
        self.level_handler = Mock()
        self.test_stage = Mock(wraps=Stage(self.window, self.player, self.score_handler, self.level_handler))
        self.test_stage.weapons = [
            Mock(),
            Mock()
        ]

    
    def test_loading_weapon_attrs_works(self):
        fireball = {
            "damage" : 20,
            "proj_speed" : 5,
            "area" : 40,
            "pierce" : 1,
            "cooldown" : 1400,
            "quantity" : 1
        }
        res = self.test_stage.load_weapon_attrs()
        self.assertEqual(fireball, res["Fireball"])
    
    def test_getting_inactive_weapons_works(self):
        res = self.test_stage.get_inactive_weapons()
        self.assertEqual(2, len(res))
        self.assertEqual("Fireball", type(res[0]).__name__)
    
    def test_getting_active_weapons_works(self):
        res = self.test_stage.get_active_weapons()
        self.assertEqual(1, len(res))
        self.assertEqual("Wand", type(res[0]).__name__)
    

        