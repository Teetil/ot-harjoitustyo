from services.wave_handler import WaveHandler
from services.randomizer import Random


class Stage():
    def __init__(self, window) -> None:
        self._wave_handler = WaveHandler(Random())
        self.enemies = []
        self._field_size = window.get_width()

    def update(self, current_time):
        if self._wave_handler.should_spawn(current_time):
            self.enemies += self._wave_handler.spawn_wave(self._field_size)
            self._wave_handler.last_move = current_time
