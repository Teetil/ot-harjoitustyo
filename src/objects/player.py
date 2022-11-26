class Player():

    def __init__(self, pos_x: int, pos_y: int, health=100, move_speed=3, damage=1) -> None:
        self._health = health
        self.move_speed = move_speed
        self.damage = damage
        self.pos_x = pos_x
        self.pos_y = pos_y

    def movement(self, pressed_key: list):
        if pressed_key[97]:
            self.pos_x -= self.move_speed
        if pressed_key[100]:
            self.pos_x += self.move_speed
        if pressed_key[119]:
            self.pos_y -= self.move_speed
        if pressed_key[115]:
            self.pos_y += self.move_speed
