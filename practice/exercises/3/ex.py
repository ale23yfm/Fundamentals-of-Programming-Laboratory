"""
Initialize a 3X3 sparse matrix
ml = SparseMatrix(3,3)
Value at [1,1] is 2
ml.set(1,1,2)
Value at [2,2] is 4
ml.set(2,2,4)
Prints
0 0 0
0 2 0
0 0 4
print(ml)
Prints class '<class 'ValueError'>'
try:
    ml.set(3,3,99)
except Exception as e:
    print(type(e))
Update value at [1,1] with 2+1
ml.set(1,1,ml.get(1,1)+1)
Prints
0 0 0
0 3 0
0 0 4
"""

class SparseMatrix:
    def __init__(self, row, col):
        self._row = row
        self._col = col
        self._matrix = {}

    def check_bound(self, r, c):
        if r < 0 or c < 0 or r >= self._row or c >= self._col:
            raise ValueError("Index out of bounds.")

    def set(self, row, col, value):
        self.check_bound(row, col)
        self._matrix[(row, col)] = value

    def get(self, row, col):
        self.check_bound(row, col)
        return self._matrix.get((row, col), 0)

    def __str__(self):
        lines = []
        for r in range(self._row):
            row = []
            for c in range(self._col):
                row.append(str(self.get(r,c)))
            lines.append(" ".join(row))
        return "\n".join(lines)


if __name__ == "__main__":
    ml = SparseMatrix(3, 3)
    ml.set(1,1,2)
    ml.set(2,2,4)
    print(ml)

    try:
        ml.set(3, 3, 99)
    except Exception as e:
        print(type(e))

    ml.set(1, 1, ml.get(1, 1) + 1)
    print(ml)