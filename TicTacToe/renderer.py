# renderer.py
from typing import Iterable
from board import Board
import os
import sys

def clear_screen() -> None:
    """Clear terminal screen (optional)."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def banner(text: str) -> None:
    """Print a simple section header (optional)."""
    line = "=" * max(len(text), 20)
    print(f"\n{line}\n{text}\n{line}")

def render(board: Board) -> None:
    """
    Render the tic-tac-toe board as a simple ASCII grid.

       0 1 2
    0  X|O| 
       -----
    1   |X| 
       -----
    2   | |O
    """
    # Column header
    print("   " + " ".join(str(i) for i in range(board.size)))
    # Rows
    for r, row in enumerate(board.grid):
        # ensure each cell is a single-character string
        cells = [(cell if isinstance(cell, str) else str(cell)) for cell in row]
        print(f"{r}  " + "|".join(cells))
        if r < board.size - 1:
            print("   " + "-" * (board.size * 2 - 1))
