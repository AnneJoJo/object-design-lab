# board.py
from typing import List, Optional

class Board:
    def __init__(self, size: int = 3):
        # use a 2D list for the grid
        self.size = size
        self.grid: List[List[str]] = [[" " for _ in range(size)] for _ in range(size)]

    def show(self) -> None:
        """Print the board in a readable format."""
        print("   " + " ".join(str(i) for i in range(self.size)))
        for r, row in enumerate(self.grid):
            print(f"{r}  " + "|".join(row))
            if r < self.size - 1:
                print("   " + "-" * (self.size * 2 - 1))

    def is_empty(self, row: int, col: int) -> bool:
        return self.grid[row][col] == " "

    def place(self, row: int, col: int, mark: str) -> None:
        if not (0 <= row < self.size and 0 <= col < self.size):
            raise ValueError("Out of bounds")
        if not self.is_empty(row, col):
            raise ValueError("Cell already taken")
        self.grid[row][col] = mark

    def available_moves(self) -> List[tuple[int, int]]:
        return [(r, c) for r in range(self.size) for c in range(self.size) if self.is_empty(r, c)]

    def is_full(self) -> bool:
        return all(self.grid[r][c] != " " for r in range(self.size) for c in range(self.size))

    def winner(self) -> Optional[str]:
        """Return 'X' or 'O' if there is a winner, else None."""
        lines = []
        # rows and columns
        for i in range(self.size):
            lines.append(self.grid[i])  # row
            lines.append([self.grid[j][i] for j in range(self.size)])  # column
        # diagonals
        lines.append([self.grid[i][i] for i in range(self.size)])
        lines.append([self.grid[i][self.size - 1 - i] for i in range(self.size)])

        for line in lines:
            if line[0] != " " and all(cell == line[0] for cell in line):
                return line[0]
        return None
    
if __name__ == "__main__":
    b = Board()
    b.place(0, 0, "X")
    b.place(1, 1, "O")
    b.show()
    print("Available:", b.available_moves())
    print("Winner:", b.winner())
