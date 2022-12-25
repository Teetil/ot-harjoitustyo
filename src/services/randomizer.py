from random import randint, choice


class Random():
    """Apuluokka satunaisuuden hallitsemiseen
    """
    def random_spawn(self, field_size: int, direction_mod: int) -> tuple:
        """Metodi joka palauttaa koordinatit johon spawnata vihollinen

        Args:
            field_size (int): Kentän leveys
            direction_mod (int): Numero joka päättää mille puolelle kenttää vihollinen syntyy

        Returns:
            tuple: Vihollisen koordinaatit
        """
        spawn_y = randint(0, field_size)
        if direction_mod % 2:
            spawn_x = 0 + randint(1, 20)
        else:
            spawn_x = field_size - 10 + randint(-20, 0)
        return spawn_x, spawn_y

    def choice_list(self, lis):
        """Palauttaa listasta yhden solun

        Args:
            lis (str): Lista joka sisältää dictionaryn avaimet, joista valitaan yksi

        Returns:
            str: string avain dictionaryyn, joka päättää mitä aseen ominaisuutta päivitetään
        """
        return choice(lis)
