

class ScoreHandler():
    def __init__(self) -> None:
        self._score = 0

    def add_score(self, base_score : int, diffculty : int):
        self._score += base_score * diffculty
    
    def get_score(self):
        return self._score
    
    def save_score(self):
        pass

    def load_score(self):
        pass
