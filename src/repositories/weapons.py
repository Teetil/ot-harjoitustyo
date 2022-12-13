import pygame
from objects.projectile import Projectile


class Weapon:
    """Luokka mistä kaikku muut aseet perivät
    """

    def __init__(self, damage, cooldown, proj_speed, area, quantity, pierce) -> None:
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
        self.damage = damage
        self.cooldown = cooldown
        self.proj_speed = proj_speed
        self.area = area
        self.quantity = quantity
        self.pierce = pierce
        self.last_shot = 0

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
        return Projectile(player.rect.centerx, player.rect.centery, enemy, self.damage, self.pierce, self.proj_speed, self.area)

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


class Wand(Weapon):
    """Ensimmäinen ase joka ampuu sinisen neliön vihollist akohti

    Args:
        Weapon (Weapon): luokka mistä ase perii
    """

    def __init__(self, damage, cooldown, proj_speed, area, quantity, pierce) -> None:
        super().__init__(damage, cooldown, proj_speed, area, quantity, pierce)


class Fireball(Weapon):
    def __init__(self, damage, cooldown, proj_speed, area, quantity, pierce) -> None:
        super().__init__(damage, cooldown, proj_speed, area, quantity, pierce)
