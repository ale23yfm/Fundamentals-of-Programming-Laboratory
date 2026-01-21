from practice.hangman.errors.errors import TextFileError

class TextFileRepo:
    def __init__(self, filepath):
        self._filepath = filepath
        self._sentences: list[str] = []
        self.load_from_file()

    def load_from_file(self):
        self._sentences.clear()
        try:
            with open(self._filepath, "r") as f:
                for l in f:
                    line = l.strip()
                    if line:
                        self._sentences.append(line)
        except FileNotFoundError as e:
            raise TextFileError from e

    def save_to_file(self):
        try:
            with open(self._filepath, "w") as f:
                for line in self._sentences:
                    f.write(line+"\n")
        except FileNotFoundError as e:
            raise TextFileError from e

    def get_all(self):
        return list(self._sentences)

    def add(self, s: str):
        self._sentences.append(s)
        self.save_to_file()