

class LevelHandler:

    def __init__(self, base_xp_requirement: int = 100, growth_mod: float = 1.3) -> None:
        self._experience = 0
        self._current_level = 1
        self._growth_mod = growth_mod
        self._base_requirement = base_xp_requirement
        self.paused = False

    def level_up(self):
        self.paused = True
        self._current_level += 1

    def should_level(self):
        if self.experience >= self.experience_requirement:
            return True
        return False

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value: int):
        self._experience = value
        if self.should_level():
            self.level_up()

    @property
    def experience_requirement(self):
        return self._base_requirement * self._current_level ** self._growth_mod
