import random


class HangmanService:
    def __init__(self, repo):
        self._repo = repo
        self._sentence = None
        self._game = False
        self._masked = []
        self._guessed = set()
        self._hangman = ""

    def add_sentence(self, s:str):
        s = s.strip().lower()
        if not s:
            raise ValueError("The sentence is empty")

        word = s.split(" ")
        for w in word:
            if len(w) < 3:
                raise ValueError("The words must contain at least 3 letters.")

        if s in self._repo.get_all():
            raise ValueError("The sentence already exists.")

        self._repo.add(s)

    def guess_letter(self, l):
        if self._game == False:
            raise ValueError("Game have not started.")

        l = l.strip().lower()
        if not l.isalpha():
            self.add_hangman()
            return

        l = l[0]

        if l in self._guessed:
            self.add_hangman()
            return

        self._guessed.add(l)
        if l not in self._sentence:
            self.add_hangman()
            return

        for i, ch in enumerate(self._sentence):
            if ch == l:
                self._masked[i] = l


    def add_hangman(self):
        if len(self._hangman) < len("hangman"):
            self._hangman = "hangman"[:len(self._hangman)+1]
        if self._hangman == "hangman":
            self._game = False

    def get_masked(self):
        return "".join(self._masked)

    def get_hangman(self):
        return self._hangman

    def is_win(self):
        if "_" in self._masked:
            return False
        return True

    def is_lost(self):
        if self._hangman == "hangman":
            return True
        return False

    def is_in_game(self):
        return self._game

    def restart(self):
        self._sentence = None
        self._game = False
        self._masked = []
        self._guessed = set()
        self._hangman = ""

    def start_game(self):
        if self._repo.get_all() == []:
            raise ValueError ("No sentences available")

        sentences = self._repo.get_all()
        self._sentence = random.choice(sentences)
        self._hangman = ""
        self._guessed = set()
        self._game = True

        self._masked = list(self._sentence)
        words = self._sentence.split()
        pos = 0

        for w in words:
            if len(w) == 3:
                pos += len(w) + 1
                continue
            first = w[0]
            last = w[-1]

            for i, ch in enumerate(w):
                if ch == first or ch == last:
                    self._masked[pos+i] = ch
                else:
                    self._masked[pos + i] = "_"
            pos += len(w) +1