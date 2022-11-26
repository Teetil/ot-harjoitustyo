class Enemy():
    def __init__(self, pos_x, pos_y, health=10, damage=1, move_speed=2) -> None:
        self._health = health
        self._damage = damage
        self._move_speed = move_speed
        self.pos_x = pos_x
        self.pos_y = pos_y
