import pygame


class FieldRenderer():

    def __init__(self, window) -> None:
        self.window = window

    def render_field(self, player, enemies: list) -> None:
        self.draw_window()
        self.draw_player(player)
        self.draw_enemy(enemies)
        pygame.display.update()

    def draw_window(self) -> None:
        self.window.fill((80, 80, 80))

    def draw_player(self, player) -> None:
        pygame.draw.rect(self.window, (0, 100, 0),
                         (player.pos_x, player.pos_y, 30, 60))

    def draw_enemy(self, enemies: list) -> None:
        for enemy in enemies:
            pygame.draw.rect(self.window, (100, 0, 0),
                             (enemy.pos_x, enemy.pos_y, 15, 15))
