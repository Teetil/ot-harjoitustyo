import pygame


class FieldRenderer():

    def __init__(self, window) -> None:
        self.window = window
        self.font = pygame.font.SysFont(None, 24)

    def render_field(self, player, enemies: list) -> None:
        self.draw_window()
        self.draw_player(player)
        self.draw_enemy(enemies)
        self.draw_text(player)
        pygame.display.update()

    def draw_window(self) -> None:
        self.window.fill((80, 80, 80))

    def draw_player(self, player) -> None:
        pygame.draw.rect(self.window, (0, 100, 0), player.rect)

    def draw_enemy(self, enemies: list) -> None:
        for enemy in enemies:
            pygame.draw.rect(self.window, (100, 0, 0), enemy.rect)

    def draw_text(self, player):
        health_text = self.font.render(str(player.health), True, (255, 0, 0))
        self.window.blit(health_text, (500, 50))