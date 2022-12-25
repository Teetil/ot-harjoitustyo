

class LevelHandler:
    """Luokka joka hallitsee pelaajan tasoa
    """

    def __init__(self, base_xp_requirement: int = 100, growth_mod: float = 1.5) -> None:
        """Luokan konstruktori

        Args:
            base_xp_requirement (int, optional): Pohja XP. tavoite, joka kasvaa joka taso growth_modin mukaan. Defaults to 100.
            growth_mod (float, optional): Muuttuja, joka kasvattaa pelaajan tarvitsemaa XP:n määrää. Defaults to 1.3.
        """
        self._experience = 0
        self._current_level = 1
        self._growth_mod = growth_mod
        self._base_requirement = base_xp_requirement
        self.paused = False

    def level_up(self):
        """Laittaa pelin tauolle estämällä mainloopin pyörimisen suurimmaksi osaksi
        """
        self.paused = True
        self._current_level += 1

    def should_level(self):
        """Metodi joka tarkistaa onko pelaajan nykyinen XP:n määrä isompi kuin tarvittava määrä

        Returns:
            bool: True jos tarpeeksi, False jos ei
        """
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
