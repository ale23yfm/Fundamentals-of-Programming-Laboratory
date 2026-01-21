from practice.labyrinth.errors.errors import TextFileError


class TextFileRepo:
    def __init__(self, filepath):
        self._filepath = filepath

    def load_from_file(self) -> list[list[int]]:
        try:
            with open(self._filepath) as f:
                text = f.readlines()
        except FileNotFoundError as e:
            raise TextFileError from e

        board: list[list[int]] = []

        for line in text:
            line = line.strip()
            if not line:
                continue

            row: list[int] = []
            for ch in line:
                row.append(int(ch))
            board.append(row)
        return board

    def save_to_file(self, board):
        try:
            with open(self._filepath, "w") as f:
                for row in board:
                    line = ""
                    for cell in row:
                        line += str(cell)
                    f.write(line+"\n")
        except OSError as e:
            raise TextFileError from e

