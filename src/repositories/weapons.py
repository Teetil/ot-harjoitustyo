import pygame
from random import choice
from objects.projectile import Projectile


class Weapon:
    """Luokka mistä kaikku muut aseet perivät
    """

    def __init__(self, damage, cooldown, proj_speed, area, quantity, pierce, active = False) -> None:
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
        self.proj_attrs = {}
        self.proj_attrs["damage"] = damage
        self.proj_attrs["proj_speed"] = proj_speed
        self.proj_attrs["area"] = area
        self.proj_attrs["pierce"] = pierce
        self.cooldown = cooldown
        self.quantity = quantity
        self.last_shot = 0
        self.active = active

    def should_shoot(self, current_time: int) -> bool:
        """Funktio joka palauttaa true jos aseen pitöisi ampua

        Args:
            current_time (int): pelin nykyinen aika jota verrataan viimeksi ammutuun aikaan

        Returns:
            bool: True jos aseen kuuluisi ampua
        """
        return current_time - self.last_shot >= self.cooldown

    def shoot_nearest(self, player, enemies: list):
        """Funktio joka palauttaa projectilen

        Args:
            player (player): Pelaaja koordinaateja varten
            enemies (list): lista vihollisista, mitä etsiä

        Returns:
            projectile: Palauttaa projectile olion, joka liikkuu lähintä vihollista päin
        """
        enemy = self.get_nearest(player, enemies)
        if not enemy:
            return None
        return Projectile((player.rect.centerx, player.rect.centery), enemy, self.color, self.proj_attrs)

    def get_nearest(self, player, enemies):
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
        return min(enemy_vect, key=lambda x: x.length())

    def upgrade_random(self):
        var_list = list(self.proj_attrs.keys())
        var_list.extend(["cooldown", "quantity"])
        var_to_upgrade = choice(var_list)
        if var_to_upgrade == "cooldown":
            self.cooldown *= 0.9
            return
        elif var_to_upgrade == "quantity":
            self.quantity += 1
            return
        self.proj_attrs[var_to_upgrade] *= 1.1


class Wand(Weapon):
    """Ensimmäinen ase joka ampuu sinisen neliön vihollist akohti

    Args:
        Weapon (Weapon): luokka mistä ase perii
    """

    def __init__(self, damage, cooldown, proj_speed, area, quantity, pierce, active = False) -> None:
        super().__init__(damage, cooldown, proj_speed, area, quantity, pierce, active)
        self.color = (0, 255, 255)


class Fireball(Weapon):
    def __init__(self, damage, cooldown, proj_speed, area, quantity, pierce, active = False) -> None:
        super().__init__(damage, cooldown, proj_speed, area, quantity, pierce, active)
        self.color = (255, 0, 0)
        self.proj_attrs["explode"] = True

class AcidPool(Weapon):
    def __init__(self, damage, cooldown, proj_speed, area, quantity, pierce, active = False) -> None:
        super().__init__(damage, cooldown, proj_speed, area, quantity, pierce, active)
        self.color = (0, 200, 0)
        self.proj_attrs["pool"] = True