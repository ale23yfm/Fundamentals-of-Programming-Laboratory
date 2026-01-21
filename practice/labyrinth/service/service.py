import random

from practice.labyrinth.errors.errors import InvalidMoveError


class GameService:
    def __init__(self, board:list[list[int]]):
        self._board=board
        self._a_pos = None
        self._m_pos = None
        self._exit_pos = None
        self._a_dir = None
        self._m_dir = None

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 9:
                    self._exit_pos = (r, c)
                    self._board[r][c] = 0

    def place_a_random(self):
        rows = len(self._board)
        cols = len(self._board[0])

        for c in range(cols):
            possible_rows = []
            for r in range(rows):
                if self._board[r][c] == 0 and (r,c) != self._exit_pos:
                    possible_rows.append(r)

            if possible_rows:
                r = random.choice(possible_rows)
                self._a_pos = (r,c)
                return

    def place_m_random(self):
        rows = len(self._board)
        cols = len(self._board[0])

        for c in range(cols - 1, -1, -1):
            possible_rows = []
            for r in range(rows):
                if self._board[r][c] == 0 and (r,c) != self._exit_pos:
                    possible_rows.append(r)

            if possible_rows:
                r = random.choice(possible_rows)
                self._m_pos = (r, c)
                return

    def move_a(self, direction, steps):
        a_pos, m_pos = self.get_positions()
        r, c = a_pos
        rm, cm = m_pos
        if direction == "up":
            dr, dc = (-1, 0)
            self._a_dir = "up"

        elif direction == "down":
            dr, dc = (1, 0)
            self._a_dir = "down"

        elif direction == "left":
            dr, dc = (0, -1)
            self._a_dir = "left"

        elif direction == "right":
            dr, dc = (0, 1)
            self._a_dir = "right"

        else: #it is move
            return self.move_a(self._a_dir, steps)

        cr, cc = r, c
        for i in range(steps):
            nr = cr+dr
            nc = cc+dc

            if not self._inside(nr, nc):
                raise InvalidMoveError
            if self._board[nr][nc] == 1:
                raise InvalidMoveError

            cr, cc = nr, nc

        self._a_pos = (cr, cc)
        return steps

    def move_m(self, steps):
        for i in range(steps):
            if self._m_pos == self._a_pos:
                return

            if self._can_see():
                self._m_dir = self.towards_a()
            else:
                if self._m_dir is None:
                    self._m_dir = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])

            dr, dc = self._m_dir
            rm, cm = self._m_pos
            nr, nc = rm + dr, cm + dc

            if (not self._inside(nr, nc)) or (not self._is_free(nr,nc)):
                dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                random.shuffle(dirs)

                moved = False
                for dr2, dc2 in dirs:
                    tr, tc = rm + dr2, cm + dc2
                    if self._inside(tr, tc) and self._is_free(tr, tc):
                        self._m_dir = (dr2, dc2)
                        self._m_pos = (tr, tc)
                        moved = True
                        break

                if not moved:
                    return  # stuck, nowhere to go

            else:
                    # 3) normal move in chosen direction
                self._m_pos = (nr, nc)

                    # 4) collision check after every step
            if self._m_pos == self._a_pos:
                return

    def towards_a(self):
        a_pos, m_pos = self.get_positions()
        r, c = a_pos
        rm, cm = m_pos

        if r == rm:
            if c > cm:
                return (0,1)
            else:
                return (0,-1)
        if c == cm:
            if r > rm:
                return (1,0)
            else:
                return (-1,0)

    def _is_free(self, r, c):
        return self._board[r][c] == 0

    def _inside(self, r, c):
        rows = len(self._board)
        cols = len(self._board[0])
        if r >= rows or c >= cols or r < 0 or c < 0:
            return False
        else:
            return True

    def _can_see(self):
        a_pos, m_pos = self.get_positions()
        r, c = a_pos
        rm, cm = m_pos
        if r == rm or c == cm:
            return True
        return False

    def get_status(self) -> str:
        a_pos, m_pos = self.get_positions()
        if a_pos == self._exit_pos:
            return "WIN"
        if a_pos == m_pos:
            return "LOSE"
        return "RUNNING"

    def get_board(self):
        return self._board

    def get_positions(self):
        return self._a_pos, self._m_pos

    def get_exit_pos(self):
        return self._exit_pos
