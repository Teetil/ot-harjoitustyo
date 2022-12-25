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
        self.level_handler.experience = 0
        self.test_stage = Stage(self.window, self.player, self.score_handler, self.level_handler)


    
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
    
    def test_updating_active_weapons_works(self):
        weapons = [Mock(), Mock(), Mock()]
        for weapon in weapons:
            weapon.active = True
            weapon.should_shoot = Mock(side_effect=[True, "called"])
            weapon.shoot_nearest = Mock(return_value=[])
        self.test_stage.update_weapons(100, weapons)
        self.assertEqual("called", weapons[0].should_shoot())
    
    def test_updating_experience_works(self):
        orbs = [Mock(), Mock(), Mock()]
        for experience in orbs:
            experience.update = Mock(side_effect=[True])
            experience.value = 10
        self.test_stage.update_experience_orbs(orbs)
        self.assertEqual(20, self.level_handler.experience)