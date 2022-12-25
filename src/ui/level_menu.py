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
            self.new_weapon()
        
        
            


    def upgrade_choice(self):
        btn1, btn2 = self.draw_choice_buttons()
        self.draw_choice_text(btn1, btn2)        
        pygame.display.update()
        click_res = self.check_click([btn1, btn2], pygame.mouse.get_pressed())
        if click_res == btn1:
            return 1
        elif click_res == btn2:
            return 2
        return 0


    def check_click(self, rects, mouse_state):
        if mouse_state[0]:
            mouse_pos = pygame.mouse.get_pos()
            for rect in rects:
                if rect.collidepoint(mouse_pos):
                    return rect
        return None
    
    def upgrade_weapons(self):
        to_upgrade = sample(self._stage.weapons, k=max(1, len(self._stage.weapons)))
        to_upgrade.sort(key=lambda x: type(x).__name__)
        rects = self.draw_weapon_upgrades(to_upgrade)
        weapons_rects = list(zip(to_upgrade, rects))
        self.draw_upgrade_text(weapons_rects)
        pygame.display.update()
        click_res = self.check_click(rects, pygame.mouse.get_pressed())
        weapon_to_upgrade = [n for n in weapons_rects if n[1] == click_res]
        if weapon_to_upgrade:
            weapon_to_upgrade[0][0].upgrade_random()
            return True
        return False


    def new_weapon(self):
        pass


    def draw_choice_buttons(self):
        btn_width = self._window.get_width() // 5
        btn_heigth = self._window.get_height() // 10
        first_btn_rect = pygame.Rect(self._window.get_width() // 2 - btn_width // 2, self._window.get_height() // 2 - btn_heigth, btn_width, btn_heigth)
        scnd_btn_rect = pygame.Rect(self._window.get_width() // 2 - btn_width // 2, self._window.get_height() // 2 + btn_heigth, btn_width, btn_heigth)
        pygame.draw.rect(self._window, self._button_color, first_btn_rect)
        pygame.draw.rect(self._window, self._button_color, scnd_btn_rect)
        return first_btn_rect, scnd_btn_rect

    def draw_choice_text(self, btn1, btn2):
        choice1 = self._font.render("Upgrade weapons", True, self._txt_color)
        choice2 = self._font.render("Choose new weapon", True, self._txt_color)
        choice1_pos = btn1.x + btn1.width // 2 - choice1.get_width() // 2, btn1.y + btn1.height // 2 - choice1.get_height() // 2
        choice2_pos = btn2.x + btn2.width // 2 - choice2.get_width() // 2, btn2.y + btn2.height // 2 - choice2.get_height() // 2
        self._window.blit(choice1, (choice1_pos))
        self._window.blit(choice2, (choice2_pos))

    def draw_weapon_upgrades(self, weapons):
        btn_width = self._window.get_width() // 3
        btn_heigth = self._window.get_height() // 10
        btn_interval = self._window.get_height() // (len(weapons) + 1)
        btn_rects = []
        for ind in range(len(weapons)):
            btn_rect = pygame.Rect(self._window.get_width() // 2 - btn_width // 2, btn_interval * (ind + 1) - btn_heigth // 2, btn_width, btn_heigth)
            btn_rects.append(btn_rect)
            pygame.draw.rect(self._window, self._button_color, btn_rect)
        return btn_rects
    
    def draw_upgrade_text(self, weapons_rects):
        for weapon, rect in weapons_rects:
            text = self._font.render(f"Upgrade random stat of {type(weapon).__name__}", True, (255, 255, 255))
            text_pos = rect.x + rect.width // 2 - text.get_width() // 2, rect.y + rect.height // 2 - text.get_height() // 2
            self._window.blit(text, (text_pos))


