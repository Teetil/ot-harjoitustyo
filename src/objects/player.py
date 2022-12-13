import pygame


class Player():
    """Luokka joka hoitaa pelaajan käyttäytymisen
    """
    def __init__(self, pos_x: int, pos_y: int, window, health=100, move_speed=3, damage=1) -> None:
        """Luokan konstruktori

        Args:
            pos_x (int): x koordinaatti
            pos_y (int): y koordinaatti
            window (pygame.surface): peli-ikkuna liikkumisen rajoittamista varten
            health (int, optional): Pelaajan maximi elämä. Defaults to 100.
            move_speed (int, optional): Pelaajan liikkumisnopeus. Defaults to 3.
            damage (int, optional): Pelaajan tekemä vahinko (turha tällä hetkellä). Defaults to 1.
        """
        self._health = health
        self.move_speed = move_speed
        self.damage = damage
        self.rect = pygame.Rect(pos_x, pos_y, 30, 60)
        self.window = window

    def movement(self, pressed_key: list):
        """Funktio joka hoitaa pelaajan liikkumisen

        Args:
            pressed_key (list): lista tällä hetkellä painetuista näppäimistä
        """
        if pressed_key[97]:
            if not self.rect.x < 0:
                self.rect.x -= self.move_speed
        if pressed_key[100]:
            if not self.rect.x > self.window.get_width() - self.rect.width:
                self.rect.x += self.move_speed
        if pressed_key[119]:
            if not self.rect.y < 0:
                self.rect.y -= self.move_speed
        if pressed_key[115]:
            if not self.rect.y > self.window.get_height() - self.rect.height:
                self.rect.y += self.move_speed

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, damage : int):
        """Pelaajan elämän asettava funktio, joka tarkistaa samalla kuolemisen

        Args:
            damage (int): vahingon määrä mikä vähentää pelaajan elämästä
        """
        self._health -= damage
        if self._health <= 0:
            pass
