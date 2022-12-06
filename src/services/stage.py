from services.wave_handler import WaveHandler
from services.randomizer import Random
from repositories.weapons import Wand


class Stage():
    def __init__(self, window, player) -> None:
        self._wave_handler = WaveHandler(Random())
        self.enemies = []
        self.player = player
        self.weapons = [Wand(10, 700, 10, 20, 1, 2)]
        self.projectiles = []
        self._field_size = window.get_width()

    def update(self, current_time):
        if self._wave_handler.should_spawn(current_time):
            self.enemies += self._wave_handler.spawn_wave(self._field_size)
            self._wave_handler.last_move = current_time
        for enemy in self.enemies:
            if enemy.update(self.player):
                self.enemies.remove(enemy)
        for weapon in self.weapons:
            if weapon.should_shoot(current_time):
                weapon.last_shot = current_time
                proj = weapon.shoot_nearest(self.player, self.enemies)
                if proj:
                    self.projectiles.append(proj)
        for projectile in self.projectiles:
            if projectile.update(self.enemies):
                self.projectiles.remove(projectile)

