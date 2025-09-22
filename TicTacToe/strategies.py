# strategies.py
import random
from typing import Tuple
from board import Board

class stretigic:
    """
    Heuristic AI for Tic-Tac-Toe.
    1) If I can win now, do it.
    2) Else if opponent can win next, block.
    3) Else random.
    """
    def __init__(self, mark: str) -> None:
        assert mark in ("X", "O")
        self.mark = mark
        self.opp = "O" if mark == "X" else "X"

    def next_move(self, board: Board) -> Tuple[int, int]:
        # helper: try move temporarily
        def would_win(r: int, c: int, m: str) -> bool:
            original = board.grid[r][c]
            board.grid[r][c] = m
            win = (board.winner() == m)
            board.grid[r][c] = original
            return win

        # 1) take winning move
        for (r, c) in board.available_moves():
            if would_win(r, c, self.mark):
                return r, c

        # 2) block opponent
        for (r, c) in board.available_moves():
            if would_win(r, c, self.opp):
                return r, c

        # 3) random choice
        return random.choice(board.available_moves())
