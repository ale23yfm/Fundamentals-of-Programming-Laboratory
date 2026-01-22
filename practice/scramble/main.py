
from pathlib import Path

from practice.scramble.repository.text_file import TextFileRepo
from practice.scramble.service.service import Service


class ConsoleUI:
    def __init__(self, service):
        self._srv = service

    def _parse_swap(self, cmd: str):
        parts = cmd.strip().split()
        # swap 0 1 - 2 3  => 6 părți
        if len(parts) != 6 or parts[0].lower() != "swap" or parts[3] != "-":
            raise ValueError("Syntax: swap <w1> <l1> - <w2> <l2>")

        try:
            w1 = int(parts[1]); l1 = int(parts[2])
            w2 = int(parts[4]); l2 = int(parts[5])
        except ValueError:
            raise ValueError("Indices must be integers.")

        return w1, l1, w2, l2

    def run(self):
        st = self._srv.start_game()
        print(self._srv.format_current(), f"[score is: {st.score}]")
        print("Commands: swap <w1> <l1> - <w2> <l2> | undo | exit")

        while True:
            if self._srv.is_won():
                st = self._srv.get_state()
                print(f"You won! Your score is {st.score}")
                return

            if self._srv.is_lost():
                print("You lost! Score reached 0.")
                return

            cmd = input(">>> ").strip()
            if cmd == "":
                continue

            try:
                low = cmd.lower()

                if low == "exit":
                    print("Bye!")
                    return

                if low == "undo":
                    st = self._srv.undo()
                    print(self._srv.format_current(), f"[score is: {st.score}]")
                    continue

                if low.startswith("swap"):
                    w1, l1, w2, l2 = self._parse_swap(cmd)
                    st = self._srv.swap_letters(w1, l1, w2, l2)
                    print(self._srv.format_current(), f"[score is: {st.score}]")
                    continue

                print("Error: Unknown command.")
            except Exception as e:
                # „nu crăpă” indiferent de input
                print(f"Error: {e}")

def main():
    path = Path(__file__).with_name("scramble.txt")
    repo = TextFileRepo(str(path))
    srv = Service(repo)
    ui = ConsoleUI(srv)
    ui.run()

if __name__ == "__main__":
    main()
