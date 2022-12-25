import unittest
from repositories.score_handler import ScoreHandler

class TestScoreHandler(unittest.TestCase):
    def test_adding_score_works(self):
        score_handler = ScoreHandler()
        score_handler.add_score(100, 1)
        self.assertEqual(100, score_handler.get_score())
    
    def test_difficulty_scaling_works(self):
        score_handler = ScoreHandler()
        score_handler.add_score(100, 5)
        self.assertEqual(500, score_handler.get_score())