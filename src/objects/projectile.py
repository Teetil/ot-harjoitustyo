import pygame


class Projectile:
    """Luokka joka hoitaa pelaajan aseiden ampumien projectilejen toiminnallisuuden
    """

    def __init__(self, coordinates : tuple, vector: pygame.Vector2, color : tuple, proj_attrs : dict) -> None:
        """Luokan konstruktori

        Args:
            coordinates (tuple): tuple muotoa (pos_x, pos_y)
            vector (pygame.Vector2): vectori lähimpään viholliseen, jonka mukaan liikkua
            color (tuple) : tuple joka sisältää projektilen rendröintivärin muodossa (R, G, B)
            proj_attrs (dict) : dictionary joka sisältää projectilen attribuutit kuten damagen ja nopeuden
        """
        self.rect = pygame.Rect(coordinates[0], coordinates[1], proj_attrs["area"], proj_attrs["area"])
        self._vector = vector
        self._proj_attrs = dict(proj_attrs)
        self.color = color
        self._hitlist = []

    def update(self, enemies: list):
        """Funktio joka hoitaa projectilen tilan muuttamisen

        Args:
            enemies (list): lista vihollisista

        Returns:
            bool: Palauttaa True jos projectile kuolee
        """
        self.move()
        if self.hit(enemies):
            if "explode" in self._proj_attrs and self._proj_attrs["explode"] == True:
                self.explode()
                return False
            if "pool" in self._proj_attrs and self._proj_attrs["pool"] == True:
                self.pool()
                return False
        if "explode" in self._proj_attrs and self._proj_attrs["explode"] == False:
            self._proj_attrs["pierce"] -= 25
        if self._proj_attrs["pierce"] <= 0:
            return True
        return False

    def move(self):
        """Liikuttaa projectilea vektoria pitkin nopeudella
        """
        self._vector.normalize()
        self._vector.scale_to_length(self._proj_attrs["proj_speed"])
        self.rect.move_ip(self._vector)

    def hit(self, enemies):
        """Funktio joka katsoo onko projecile osumassa viholliseen, tällä hetkellä

        Args:
            enemies (list): lista vihollisia
        """
        has_hit = False
        collidelist = self.rect.collidelistall(enemies)
        for index in collidelist:
            if self._proj_attrs["pierce"] > 0 and enemies[index] not in self._hitlist:
                self._proj_attrs["pierce"] -= 1
                enemies[index].health = self._proj_attrs["damage"]
                self._hitlist.append(enemies.index)
                has_hit = True
        return has_hit


    def explode(self,):
        self.rect.inflate_ip(self._proj_attrs["area"] * 2, self._proj_attrs["area"] * 2)
        self._proj_attrs["proj_speed"] = 0.1
        self._proj_attrs["pierce"] = 100
        self._proj_attrs["explode"] = False

    def pool(self):
        self.rect.inflate_ip(self._proj_attrs["area"] * 1.5, self._proj_attrs["area"] * 1.5)
        self._proj_attrs["proj_speed"] = 0.1
        self._proj_attrs["pierce"] = 10
        self._proj_attrs["pool"] = False
