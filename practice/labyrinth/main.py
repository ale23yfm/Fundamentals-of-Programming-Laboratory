from texttable import Texttable
from pathlib import Path

from practice.labyrinth.service.service import GameService
from practice.labyrinth.repository.text_file import TextFileRepo
from practice.labyrinth.errors.errors import TextFileError, InvalidMoveError


def render(board, a_pos, m_pos, exit_pos):
    rows = len(board)
    cols = len(board[0])

    table = Texttable()
    table.set_cols_align(["c"]*cols)
    table.set_cols_valign(["m"]*cols)

    for r in range(rows):
        line = []
        for c in range(cols):
            if (r, c) == a_pos:
                line.append("A")
            elif (r, c) == m_pos:
                line.append("M")
            elif (r, c) == exit_pos:
                line.append("-")
            else:
                cell = board[r][c]
                if cell == 1:
                    line.append("X")
                else:
                    line.append(" ")
        table.add_row(line)
    print(table.draw())


def main():
    lab_path = Path(__file__).with_name("labyrinth.txt")
    repo = TextFileRepo(str(lab_path))

    try:
        board = repo.load_from_file()
    except TextFileError:
        print("Error reading/writing labyrinth file.")
        return

    service = GameService(board)
    service.place_a_random()
    service.place_m_random()

    print ("Welcome to the game. Make Ariadne win!")
    while True:
        a_pos, m_pos = service.get_positions()
        exit_pos = service.get_exit_pos()
        status = service.get_status()
        render(board, a_pos, m_pos, exit_pos)

        if status == "WIN":
            print("Ariadne won!")
            break
        if status == "LOSE":
            print("Minotaur won!")
            break

        cmd = input("Command (up/right/down/left/move/move n/exit): ").strip().lower()
        direction_cmds = {"up", "down", "left", "right"}
        part = cmd.split()

        if part[0] == "exit":
            print("Thanks for trying")
            break

        elif part[0] in direction_cmds:
            direction = part[0]
            steps = 1

        elif part[0] == "move":
            direction = None
            if len(part) == 1:
                steps = 1
            elif len(part) == 2:
                steps = int(part[1])
                try:
                    if steps <= 0:
                        print("Number of steps must be positive.")
                        continue
                except ValueError:
                    print ("Invalid command")
                    continue
        else:
            print("Invalid command. Try again with 'up/right/down/left/move/move n/exit'")
            continue

        try:
            moved_steps=service.move_a(direction, steps)
            service.move_m(moved_steps)
        except InvalidMoveError:
            print("Invalid move (wall/outside or not direction yet). Try again.")
            continue

if __name__ == "__main__":
    main()
