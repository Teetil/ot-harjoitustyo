from json import load
from pathlib import Path


class DataHandler:
    """Apuluokka noutamaan aseiden pohja attribuutit JSON tiedostosta

    Returns:
        dict: dictionary joka sisältää aseiden tiedot
    """
    @staticmethod
    def load_weapon_attrs(filename: str,) -> dict:
        """Metodi joka hoitaa hakemisen

        Args:
            filename (str): JSON tiedoston nimi

        Returns:
            dict: dictionary joka sisältää aseiden tiedot
        """
        filepath = Path(__file__).parent / f"../data/{filename}"
        with open(filepath, "r", encoding="utf-8") as file:
            return load(file)
