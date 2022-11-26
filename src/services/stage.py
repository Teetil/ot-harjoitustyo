from services.wave_handler import WaveHandler
from services.randomizer import Random


class Stage():
    def __init__(self, window) -> None:
        self._waveHandler = WaveHandler(Random())
        self.enemies = []
        self._fieldSize = window.get_width()
    
    def update(self, current_time):
        if self._waveHandler.should_spawn(current_time):
            self.enemies += self._waveHandler.spawnWave(self._fieldSize)
            self._waveHandler.lastMove = current_time