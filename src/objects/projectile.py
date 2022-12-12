import pygame


class Projectile:
    """Luokka joka hoitaa pelaajan aseiden ampumien projectilejen toiminnallisuuden
    """
    def __init__(self, pos_x: int, pos_y: int, vector: pygame.Vector2, damage: int, pierce: int, proj_speed : int, area: int) -> None:
        """Luokan konstruktori

        Args:
            pos_x (int): x koordinaatti
            pos_y (int): y koordinaatti
            vector (pygame.Vector2): vectori lähimpään viholliseen, jonka mukaan liikkua
            damage (int): vahingon määrä viholliseen
            pierce (int): kuinka moneen viholliseen pojectile voi osua ennen kuolemaa
            proj_speed (int): projectilen nopeus    
            area (int): Projectilen koko
        """
        self.rect = pygame.Rect(pos_x, pos_y, area, area)
        self._vector = vector
        self._damage = damage
        self._pierce = pierce
        self._proj_speed = proj_speed
        self._hitlist = []

    def update(self, enemies : list):
        """Funktio joka hoitaa projectilen tilan muuttamisen

        Args:
            enemies (list): lista vihollisista

        Returns:
            bool: Palauttaa True jos projectile kuolee
        """
        self.move()
        self.hit(enemies)
        if self._pierce == 0:
            return True
        return False

    def move(self):
        """Liikuttaa projectilea vektoria pitkin nopeudella
        """
        self._vector.normalize()
        self._vector.scale_to_length(self._proj_speed)
        self.rect.move_ip(self._vector)

    def hit(self, enemies):
        """Funktio joka katsoo onko projecile osumassa viholliseen, tällä hetkellä

        Args:
            enemies (lis): lista vihollisia
        """
        collidelist = self.rect.collidelistall(enemies)
        for index in collidelist:
            if self._pierce > 0:
                self._pierce -= 1
                enemies[index].health = self._damage
