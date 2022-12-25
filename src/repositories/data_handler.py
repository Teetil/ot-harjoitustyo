from json import load
from pathlib import Path


class DataHandler:

    @staticmethod
    def load_weapon_attrs(filename: str,) -> dict:
        filepath = Path(__file__).parent / f"../data/{filename}"
        with open(filepath, "r", encoding="utf-8") as file:
            return load(file)
