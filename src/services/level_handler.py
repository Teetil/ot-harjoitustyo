

class LevelHandler:

    def __init__(self, base_xp_requirement : int = 100, growth_mod : float = 1.5) -> None:
        self._experience = 0
        self._current_level = 1
        self._growth_mod = growth_mod
        self._base_requirement = base_xp_requirement

    def level_up(self):
        pass

    def should_level(self):
        if self.experience >= self._base_requirement * self._growth_mod * self._current_level:
            return True
        return False

    @property
    def experience(self):
        return self._experience
    
    @experience.setter
    def experience(self, value : int):
        self._experience += value
        if self.should_level():
            self.level_up()
