from services.wave_handler import WaveHandler
from services.randomizer import Random
from repositories.weapons import Wand


class Stage():
    """Luokka joka hoitaa pelikentän toiminallisuuden
    """
    def __init__(self, window, player, score_handler) -> None:
        """Luokan konstruktori

        Args:
            window (pygame.surface): surface jolle peli piirretään
            player (player): kentän pelaaja
        Attributes:
            wave_handler: luokka joka hoitaa vihollisten syntymisen
            score_handler: luokka joka hallitsee pisteiden saamista
            enemies: lista hengissä olevista vihollisista kentälä
            weapons: pelaajan omaavat aseet
            projectiles: lista elävistä projectileista
            field_size: kentän koko
            difficulty_mod: numero, millä lisätä vihollisten nopeutta ja elämää

        """
        self._wave_handler = WaveHandler(Random())
        self._score_handler = score_handler
        self.enemies = []
        self.player = player
        self.weapons = [Wand(10, 700, 10, 20, 1, 2)]
        self.projectiles = []
        self._field_size = window.get_width()
        self.difficulty_mod = 1

    def update(self, current_time):
        """Päivittää kaikki kentällä olevat oliot

        Args:
            current_time (int): tämän hetkinen aika
        
        Returns:
            bool: True jos pelaaja elossa, False jos kuollut
        """
        if self._wave_handler.should_spawn(current_time):
            self.enemies += self._wave_handler.spawn_wave(self._field_size, self.difficulty_mod)
            self._wave_handler.last_move = current_time
        for enemy in self.enemies:
            if enemy.update(self.player):
                self.enemies.remove(enemy)
                self._score_handler.add_score(10, self.difficulty_mod)
        for weapon in self.weapons:
            if weapon.should_shoot(current_time):
                weapon.last_shot = current_time
                proj = weapon.shoot_nearest(self.player, self.enemies)
                if proj:
                    self.projectiles.append(proj)
        for projectile in self.projectiles:
            if projectile.update(self.enemies):
                self.projectiles.remove(projectile)
        if self.player.health <= 0:
            return False
        return True
