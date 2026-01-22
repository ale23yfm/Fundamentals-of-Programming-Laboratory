import random
from practice.scramble.errors.errors import TextFileError


class TextFileRepo:
    def __init__(self, filepath):
        self._filepath = filepath
        self._sentences = []
        self.load_from_file()

    def load_from_file(self):
        try:
            with open(self._filepath, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        self._sentences.append(line)
        except FileNotFoundError as e:
            raise TextFileError from e

        # OPTIONAL dar recomandat pt cerință:
        if len(self._sentences) < 5:
            raise TextFileError("Input file must contain at least 5 sentences.")

    def get_all(self):
        return list(self._sentences)

    def get_random_sentence(self):
        return random.choice(self._sentences)
