import unittest
from services.main_loop import MainLoop

class TestMainLopp(unittest.TestCase):
    def setUp(self) -> None:
        self.mainLoop = MainLoop()
    
        