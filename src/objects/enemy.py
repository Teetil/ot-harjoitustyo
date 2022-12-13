import pygame


class Enemy():
    """Luokka, joka kuvaa vihollisia ja niiden toimitaa
    Attributes:
        health: Vihollisten elämä, jos 0 -> kuolema
        damage: Vihollisten tekemä vanhinko pelaajaan osuessa
        move_speed: Vihollisten nopeus
        rect: Vihollista kuvaava neliö pygamessa
    """
    def __init__(self, pos_x, pos_y, health=10, damage=1, move_speed=2) -> None:
        """luokan konstruktori, joka luo uuden vihollisen

        Args:
            pos_x (int): x koordinaatti
            pos_y (y): y koordinaatti
            health (int, optional): Defaults to 10.
            damage (int, optional): Defaults to 1.
            move_speed (int, optional): Defaults to 2.
        """
        self._health = health
        self._damage = damage
        self._move_speed = move_speed
        self.rect = pygame.Rect(pos_x, pos_y, 15, 30)

    def update(self, player):
        """funktio joka päivittää ja tarkastaa vihollisen tilan

        Args:
            player (Player): pelaaja luokka, jotta vihollinen voi liikkua pelaaja kohti ja tehdä siihen vahinkoa

        Returns:
            bool: Palautta onko vihollinen kuollut vai ei
        """
        self.move(player)
        self.damage(player)
        if self.health <= 0:
            return True
        return False

    def move(self, player) -> None:
        """Funktio joka liikuttaa vihollista

        Args:
            player (Player): pelaaja jota päin liikkua

        Returns:
            bool: Palauttaa True jos liikkuminen onnistui ja False jos ei tarvitse liikkua ja on jo pelaajan sisällä
        """     
        dirvect = pygame.math.Vector2(
            player.rect.centerx - self.rect.centerx, player.rect.centery - self.rect.centery)
        if dirvect.length() == 0:
            return False
        dirvect.normalize()
        dirvect.scale_to_length(self._move_speed)
        self.rect.move_ip(dirvect)
        return True

    def damage(self, player):
        """Funktio jolla vihollinen tekee vahinkoa pelaajaan

        Args:
            player (Player()): Pelaaja johon tehdä vahinko
        """
        if self.rect.colliderect(player.rect):
            player.health = self._damage

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, damage):
        self._health -= damage
