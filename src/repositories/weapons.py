from math import ceil
import pygame
from objects.projectile import Projectile


class Weapon:
    """Luokka mistä kaikku muut aseet perivät
    """

    def __init__(self, weapon_attrs, randomizer, active=False, color=None,) -> None:
        """Luokan konstruktori

        Args:
            damage (int): aseen tekemä vahinko
            cooldown (int): aika aseen ampumisien välillä
            proj_speed (int): aseen ampuvan projectilen npeus
            area (int): aseen ampuvan projectilen koko
            quantity (int): kuinka monta projectilea ase ampuu
            pierce (int): kuinka monen vihollisen läpi projectilet menevät
        Attributes:
            last_shot: aika milloin viimeinen ammunta tapahtui
        """
        self.proj_attrs = dict(weapon_attrs)
        self._cooldown = weapon_attrs["cooldown"]
        self._quantity = weapon_attrs["quantity"]
        self.last_shot = 0
        self.active = active
        self.color = color
        self._randomizer = randomizer

    def should_shoot(self, current_time: int) -> bool:
        """Funktio joka palauttaa true jos aseen pitöisi ampua

        Args:
            current_time (int): pelin nykyinen aika jota verrataan viimeksi ammutuun aikaan

        Returns:
            bool: True jos aseen kuuluisi ampua
        """
        return current_time - self.last_shot >= self._cooldown

    def shoot_nearest(self, player, enemies: list) -> list:
        """Funktio joka palauttaa projectilen

        Args:
            player (player): Pelaaja koordinaateja varten
            enemies (list): lista vihollisista, mitä etsiä

        Returns:
            list (Projectile): Palauttaa projectile lista, jotka liikkuvat lähimpiä viholisia päin
        """
        enemies = self._get_nearest(player, enemies)
        if not enemies:
            return []
        projectiles = []
        for enemy in enemies:
            projectiles.append(
                Projectile((player.rect.centerx, player.rect.centery),
                           enemy, self.color, self.proj_attrs)
            )
        return projectiles

    def _get_nearest(self, player, enemies):
        """Funktio joka palauttaa vektorin lähintä vihollista kohti

        Args:
            player (player): pelaaja koordinaatteja varten
            enemies (list): lista vihollisista

        Returns:
            pygame.vector: palauttaa lyhyimmän vektorin joka on samalla lähin vihollinen
        """
        if not enemies:
            return None
        enemy_vect = []
        for enemy in enemies:
            enemy_vect.append(pygame.math.Vector2(
                enemy.rect.centerx - player.rect.centerx, enemy.rect.centery - player.rect.centery))
        enemy_vect.sort(key=lambda n: n.length())
        return enemy_vect[0:ceil(self._quantity)]

    def upgrade_random(self):
        """Funktio joka päivittää prosentuaalisesti satunnaista aseen ominaisuutta
        """
        var_list = list(self.proj_attrs.keys())
        var_list.extend(["cooldown", "quantity"])
        var_to_upgrade = self._randomizer.choice_list(var_list)
        if var_to_upgrade == "cooldown":
            self._cooldown *= 0.9
            return
        if var_to_upgrade == "quantity":
            self._quantity += 1
            return
        self.proj_attrs[var_to_upgrade] *= 1.3


class Wand(Weapon):
    """Ensimmäinen ase joka ampuu sinisen neliön vihollist akohti

    Args:
        Weapon (Weapon): luokka mistä ase perii
    """

    def __init__(self, weapon_attrs, randomizer, active=False) -> None:
        super().__init__(weapon_attrs, randomizer, active)
        self.color = (0, 255, 255)


class Fireball(Weapon):
    """Ase joka ampuu hitaammin punaisen pallon joka laajenee osuessaan viholliseen ja katoaa

    Args:
        Weapon (Weapon): luokka mistä ase perii
    """
    def __init__(self, weapon_attrs, randomizer, active=False) -> None:
        super().__init__(weapon_attrs, randomizer, active)
        self.color = (255, 0, 0)
        self.proj_attrs["explode"] = True


class AcidPool(Weapon):
    """Ase joka ampuu viherän pallon joka luo pysyvän ansan maahan kunnes se tekee vahinkonsa loppuun

    Args:
        Weapon (Weapon): Luokka josta ase perii
    """
    def __init__(self, weapon_attrs, randomizer, active=False) -> None:
        super().__init__(weapon_attrs, randomizer, active)
        self.color = (0, 200, 0)
        self.proj_attrs["pool"] = True
