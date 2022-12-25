from random import randint, choice


class Random():
    def random_spawn(self, field_size: int, direction_mod: int) -> tuple:
        spawn_y = randint(0, field_size)
        if direction_mod % 2:
            spawn_x = 0 + randint(1, 20)
        else:
            spawn_x = field_size - 10 + randint(-20, 0)
        return spawn_x, spawn_y

    def choice_list(self, lis):
        return choice(lis)
