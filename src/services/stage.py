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
            weapon_attrs: JSON tiedostosta ladatut aseiden aloitusatribuutit
            weapons: pelaajan omaavat aseet
            projectiles: lista elävistä projectileista
            experience_gems: lista olemassa olevista experince olioista
            field_size: kentän koko
            difficulty_stat: tuple josta ensimmäinen luku on nykyinen vaikeustaso ja toinen luku kuinka osen taso nuosee millisekuneissa

        """
        self._window = window
        self._wave_handler = WaveHandler(Random())
        self._score_handler = score_handler
        self._level_handler = level_handler
        self.enemies = []
        self.player = player
        weapon_attrs = self._load_weapon_attrs()

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
        self._update_enemies()
        self._update_weapons(current_time, self.weapons)
        self._update_projectiles()
        self._update_experience_orbs(self.experience_gems)
        if self._should_scale_difficulty(current_time):
            self._difficulty_stat = self._difficulty_stat[0] + \
                1, self._difficulty_stat[1]
        if self.player.health <= 0:
            return False
        return True

    def _update_enemies(self):
        for enemy in self.enemies:
            if enemy.update(self.player):
                self.experience_gems.append(Experience(
                    (enemy.rect.x, enemy.rect.y), self._difficulty_stat[0]))
                self.enemies.remove(enemy)
                self._score_handler.add_score(10, self._difficulty_stat[0])

    def _update_weapons(self, current_time, weapons):
        projectiles = []
        for weapon in weapons:
            if weapon.active and weapon.should_shoot(current_time):
                weapon.last_shot = current_time
                projectiles = weapon.shoot_nearest(self.player, self.enemies)
                for proj in projectiles:
                    self.projectiles.append(proj)

    def _update_projectiles(self):
        for projectile in self.projectiles:
            if projectile.update(self.enemies):
                self.projectiles.remove(projectile)

    def _update_experience_orbs(self, experience_gems):
        to_remove = []
        for experience in experience_gems:
            if experience.update(self.player):
                self._level_handler.experience += experience.value
                to_remove.append(experience)
        for experience in to_remove:
            experience_gems.remove(experience)

    def _should_scale_difficulty(self, current_time):
        return current_time - self._difficulty_stat[1] * self._difficulty_stat[0] > 0

    def get_active_weapons(self):
        """Apumetodi joka hakee kaikki tällä hetkellä aktiiviset pelaajan aseet

        Returns:
            list: lista aktiivisista aseista
        """
        return [weapon for weapon in self.weapons if weapon.active]

    def get_inactive_weapons(self):
        """Apumetodi joka hakee kaikki tällä hetkellä inactiiviset pelaajan aseet

        Returns:
            list: lista inaktiivisista aseista
        """
        return [weapon for weapon in self.weapons if not weapon.active]

    def _load_weapon_attrs(self):
        return DataHandler.load_weapon_attrs(r"default_stats.json")
