import pygame
from random import sample


class LevelMenu:
    def __init__(self, window, stage) -> None:
        self._window = window
        self._stage = stage
        self._font = pygame.font.SysFont(None, 24)
        self._button_color = (100, 100, 100)
        self._txt_color = (255, 255, 255)
        self.decision = 0

    def level_up_menu(self):
        self._window.fill((0, 0, 0))
        if not self.decision:
            self.decision = self.upgrade_choice()
            return
        elif self.decision == 1:
            return self.upgrade_weapons()
        elif self.decision == 2:
            return self.new_weapon()
        elif self.decision == 3:
            self.decision = 0
            return self._stage.player.heal_to_full()

    def upgrade_choice(self):
        buttons = self.draw_choice_buttons()
        self.draw_choice_text(buttons)
        pygame.display.update()
        click_res = self.check_click(buttons, pygame.mouse.get_pressed())
        if click_res == buttons[0]:
            return 1
        elif click_res == buttons[1]:
            return 2
        elif len(buttons) > 2 and click_res == buttons[2]:
            return 3
        elif len(buttons) < 2 and click_res == buttons[1]:
            return 3
        return 0

    def check_click(self, rects, mouse_state):
        if mouse_state[0]:
            mouse_pos = pygame.mouse.get_pos()
            for rect in rects:
                if rect.collidepoint(mouse_pos):
                    return rect
        return None

    def upgrade_weapons(self):
        active = self._stage.get_active_weapons()
        to_upgrade = sample(active, k=max(1, len(active)))
        to_upgrade.sort(key=lambda x: type(x).__name__)
        weapon_to_upgrade = self.draw_weapon_level_up(to_upgrade)
        if weapon_to_upgrade:
            weapon_to_upgrade[0][0].upgrade_random()
            self.decision = 0
            return True
        return False

    def new_weapon(self):
        non_active = self._stage.get_inactive_weapons()
        new_weapon = self.draw_weapon_level_up(non_active)
        if new_weapon:
            new_weapon[0][0].active = True
            self.decision = 0
            return True
        return False

    def draw_weapon_level_up(self, weapons: list):
        rects = self.draw_weapon_upgrades(weapons)
        weapons_rects = list(zip(weapons, rects))
        self.draw_weapon_text(weapons_rects)
        pygame.display.update()
        click_res = self.check_click(rects, pygame.mouse.get_pressed())
        return [n for n in weapons_rects if n[1] == click_res]

    def draw_choice_buttons(self):
        rects = []
        btn_width = self._window.get_width() // 5
        btn_heigth = self._window.get_height() // 10
        first_btn_rect = pygame.Rect(self._window.get_width(
        ) // 2 - btn_width // 2, self._window.get_height() // 2 - btn_heigth*2, btn_width, btn_heigth)
        scnd_btn_rect = pygame.Rect(self._window.get_width(
        ) // 2 - btn_width // 2, self._window.get_height() // 2 + btn_heigth*2, btn_width, btn_heigth)
        rects.append(first_btn_rect)
        rects.append(scnd_btn_rect)
        if self._stage.get_inactive_weapons():
            third_btn_rect = pygame.Rect(self._window.get_width(
            ) // 2 - btn_width // 2, self._window.get_height() // 2, btn_width, btn_heigth)
            rects.append(third_btn_rect)
        for rect in rects:
            pygame.draw.rect(self._window, self._button_color, rect)
        return rects

    def draw_choice_text(self, buttons):
        choice1 = self._font.render("Upgrade weapons", True, self._txt_color)
        choice2 = self._font.render("Choose new weapon", True, self._txt_color)
        choice3 = self._font.render("Heal to full hp", True, self._txt_color)
        choice1_pos = buttons[0].x + buttons[0].width // 2 - choice1.get_width(
        ) // 2, buttons[0].y + buttons[0].height // 2 - choice1.get_height() // 2
        if len(buttons) > 2:
            choice2_pos = buttons[1].x + buttons[1].width // 2 - choice2.get_width(
            ) // 2, buttons[1].y + buttons[1].height // 2 - choice2.get_height() // 2
            choice3_pos = buttons[2].x + buttons[2].width // 2 - choice3.get_width(
            ) // 2, buttons[2].y + buttons[2].height // 2 - choice3.get_height() // 2
            self._window.blit(choice2, (choice2_pos))
        else:
            choice3_pos = buttons[1].x + buttons[1].width // 2 - choice3.get_width(
            ) // 2, buttons[1].y + buttons[1].height // 2 - choice3.get_height() // 2
        self._window.blit(choice3, (choice3_pos))
        self._window.blit(choice1, (choice1_pos))

    def draw_weapon_upgrades(self, weapons):
        btn_width = self._window.get_width() // 3
        btn_heigth = self._window.get_height() // 10
        btn_interval = self._window.get_height() // (len(weapons) + 1)
        btn_rects = []
        for ind in range(len(weapons)):
            btn_rect = pygame.Rect(self._window.get_width(
            ) // 2 - btn_width // 2, btn_interval * (ind + 1) - btn_heigth // 2, btn_width, btn_heigth)
            btn_rects.append(btn_rect)
            pygame.draw.rect(self._window, self._button_color, btn_rect)
        return btn_rects

    def draw_upgrade_text(self, weapons_rects):
        for weapon, rect in weapons_rects:
            text = self._font.render(
                f"Upgrade random stat of {type(weapon).__name__}", True, (255, 255, 255))
            text_pos = rect.x + rect.width // 2 - text.get_width() // 2, rect.y + \
                rect.height // 2 - text.get_height() // 2
            self._window.blit(text, (text_pos))

    def draw_new_weapon_text(self, weapon_rects: list):
        for weapon, rect in weapon_rects:
            text = self._font.render(
                f"Upgrade random stat of {type(weapon).__name__}", True, (255, 255, 255))
            text_pos = rect.x + rect.width // 2 - text.get_width() // 2, rect.y + \
                rect.height // 2 - text.get_height() // 2
            self._window.blit(text, (text_pos))

    def draw_weapon_text(self, weapon_rects):
        for weapon, rect in weapon_rects:
            if weapon.active:
                text = self._font.render(
                    f"Upgrade random stat of {type(weapon).__name__}", True, (255, 255, 255))
            elif not weapon.active:
                text = self._font.render(
                    f"Add {type(weapon).__name__} to player", True, (255, 255, 255))
            text_pos = rect.x + rect.width // 2 - text.get_width() // 2, rect.y + \
                rect.height // 2 - text.get_height() // 2
            self._window.blit(text, (text_pos))
