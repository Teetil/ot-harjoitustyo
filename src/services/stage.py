from services.wave_handler import WaveHandler
from services.randomizer import Random
from repositories.weapons import Wand, Fireball, AcidPool
from repositories.data_handler import DataHandler
from objects.experience import Experience


class Stage():
    """Luokka joka hoitaa pelikentän toiminallisuuden
    """

    def __init__(self, window, player, score_handler, level_handler) -> None:
        """Luokan konstruktori

        Args:
            window (pygame.surface): surface jolle peli piirretään
            player (player): kentän pelaaja
        Attributes:
            wave_handler: luokka joka hoitaa vihollisten syntymisen
            score_handler: luokka joka hallitsee pisteiden saamista
            level_handler: luokka joka hallitsee pelaajan experiencen ja levelin
            enemies: lista hengissä olevista vihollisista kentälä
            weapons: pelaajan omaavat aseet
            projectiles: lista elävistä projectileista
            experience_gems: lista olemassa olevista experince olioista
            field_size: kentän koko
            difficulty_mod: numero, millä lisätä vihollisten nopeutta ja elämää

        """
        self._window = window
        self._wave_handler = WaveHandler(Random())
        self._score_handler = score_handler
        self._level_handler = level_handler
        self.enemies = []
        self.player = player
        weapon_attrs = self.load_weapon_attrs()

        self.weapons = [
            Fireball(weapon_attrs["Fireball"], Random()),
            AcidPool(weapon_attrs["AcidPool"], Random()),
            Wand(weapon_attrs["Wand"], Random(), active=True)
        ]
        self.projectiles = []
        self.experience_gems = []
        self._field_size = self._window.get_width()
        self._difficulty_stat = (1, 20000)

    def update(self, current_time):
        """Päivittää kaikki kentällä olevat oliot

        Args:
            current_time (int): tämän hetkinen aika

        Returns:
            bool: True jos pelaaja elossa, False jos kuollut
        """
        if self._wave_handler.should_spawn(current_time, self._difficulty_stat[0]):
            self.enemies += self._wave_handler.spawn_wave(
                self._field_size, self._difficulty_stat[0])
            self._wave_handler.last_move = current_time
        self.update_enemies()
        self.update_weapons(current_time)
        self.update_projectiles()
        self.update_experience_orbs()
        if self.should_scale_difficulty(current_time):
            self._difficulty_stat = self._difficulty_stat[0] + \
                1, self._difficulty_stat[1]
        if self.player.health <= 0:
            return False
        return True

    def update_enemies(self):
        for enemy in self.enemies:
            if enemy.update(self.player):
                self.experience_gems.append(Experience(
                    (enemy.rect.x, enemy.rect.y), self._difficulty_stat[0]))
                self.enemies.remove(enemy)
                self._score_handler.add_score(10, self._difficulty_stat[0])

    def update_weapons(self, current_time):
        for weapon in self.weapons:
            if weapon.active and weapon.should_shoot(current_time):
                weapon.last_shot = current_time
                projectiles = weapon.shoot_nearest(self.player, self.enemies)
                if projectiles:
                    for proj in projectiles:
                        self.projectiles.append(proj)

    def update_projectiles(self):
        for projectile in self.projectiles:
            if projectile.update(self.enemies):
                self.projectiles.remove(projectile)

    def update_experience_orbs(self):
        for experience in self.experience_gems:
            if experience.update(self.player):
                self._level_handler.experience += experience.value
                self.experience_gems.remove(experience)

    def should_scale_difficulty(self, current_time):
        return current_time - self._difficulty_stat[1] * self._difficulty_stat[0] > 0

    def get_active_weapons(self):
        return [weapon for weapon in self.weapons if weapon.active]

    def get_inactive_weapons(self):
        return [weapon for weapon in self.weapons if not weapon.active]

    def load_weapon_attrs(self):
        return DataHandler.load_weapon_attrs(r"default_stats.json")
