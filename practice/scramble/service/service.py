from practice.scramble.domain.scramble import GameState
from practice.scramble.errors.errors import TextFileError  # doar dacă vrei
# ideal: definește și InvalidSwapError, dar dacă nu ai, folosim ValueError

import random


class Service:
    def __init__(self, repo):
        self._repo = repo
        self._state = None

    def get_state(self):
        if self._state is None:
            raise ValueError("Game not started.")
        return self._state

    def start_game(self):
        sentence = self._repo.get_random_sentence()
        target_words = sentence.split()  # split simplu (spații multiple ok)

        current_words = self.keep_ends(target_words)
        score = sum(len(w) for w in target_words)

        self._state = GameState(target_words, current_words, score)
        return self._state

    def keep_ends(self, words: list[str]):
        middle = []
        for w in words:
            if len(w) > 2:
                for ch in w[1:-1]:
                    middle.append(ch)

        random.shuffle(middle)

        result = []
        pos = 0
        for w in words:
            if len(w) <= 2:
                result.append(w)
            else:
                length = len(w) - 2
                mid = ""
                for i in range(length):
                    mid += middle[pos]
                    pos += 1
                nw = w[0] + mid + w[-1]
                result.append(nw)

        return result

    def _validate_pos(self, words: list[str], wi: int, li: int):
        if wi < 0 or wi >= len(words):
            raise ValueError("Invalid word index.")
        if li < 0 or li >= len(words[wi]):
            raise ValueError("Invalid letter index.")
        if li == 0 or li == len(words[wi]) - 1:
            raise ValueError("Cannot swap first/last letter.")

    def swap_letters(self, w1: int, l1: int, w2: int, l2: int):
        st = self.get_state()

        self._validate_pos(st.current_words, w1, l1)
        self._validate_pos(st.current_words, w2, l2)

        if st.score <= 0:
            return st

        cw = st.current_words[:]  # copie listă
        a = list(cw[w1])
        b = list(cw[w2])

        a[l1], b[l2] = b[l2], a[l1]

        cw[w1] = "".join(a)
        cw[w2] = "".join(b)

        st.current_words = cw
        st.score -= 1
        st.undo_stack.append((w1, l1, w2, l2))
        return st

    def undo(self):
        st = self.get_state()
        if not st.undo_stack:
            return st

        w1, l1, w2, l2 = st.undo_stack.pop()

        cw = st.current_words[:]
        a = list(cw[w1])
        b = list(cw[w2])

        a[l1], b[l2] = b[l2], a[l1]

        cw[w1] = "".join(a)
        cw[w2] = "".join(b)
        st.current_words = cw

        # scorul NU se schimbă la undo
        return st

    def is_won(self):
        st = self.get_state()
        return st.current_words == st.target_words

    def is_lost(self):
        st = self.get_state()
        return st.score <= 0

    def format_current(self):
        st = self.get_state()
        return " ".join(st.current_words)
