import pygame
from objects.projectile import Projectile


class Weapon:
    def __init__(self, damage, cooldown, proj_speed, area, quantity, pierce) -> None:
        self.damage = damage
        self.cooldown = cooldown
        self.proj_speed = proj_speed
        self.area = area
        self.quantity = quantity
        self.pierce = pierce
        self.last_shot = 0

    def should_shoot(self, current_time: int) -> bool:
        return current_time - self.last_shot >= self.cooldown

    def shoot_nearest(self, player, enemies: list):
        enemy = self.get_nearest(player, enemies)
        if not enemy:
            return None
        return Projectile(player.rect.centerx, player.rect.centery, enemy, self.damage, self.pierce, self.proj_speed, self.area)

    def get_nearest(self, player, enemies):
        if not enemies:
            return None
        enemy_vect = []
        for enemy in enemies:
            enemy_vect.append(pygame.math.Vector2(
                enemy.rect.centerx - player.rect.centerx, enemy.rect.centery - player.rect.centery))
        return min(enemy_vect, key=lambda x: x.length())


class Wand(Weapon):
    def __init__(self, damage, cooldown, proj_speed, area, quantity, pierce) -> None:
        super().__init__(damage, cooldown, proj_speed, area, quantity, pierce)


class Fireball(Weapon):
    def __init__(self, damage, cooldown, proj_speed, area, quantity, pierce) -> None:
        super().__init__(damage, cooldown, proj_speed, area, quantity, pierce)
