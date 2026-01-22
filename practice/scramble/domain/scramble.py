class GameState:
    def __init__(self, target_words, current_words, score):
        self.target_words = target_words
        self.current_words = current_words
        self.score = score
        self.undo = []