# players.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Tuple
import random

from board import Board

# We assume a minimal Board implementation like the one you wrote:
# class Board:
#     size: int
#     grid: list[list[str]]
#     def is_empty(self, r:int, c:int) -> bool: ...
#     def place(self, r:int, c:int, mark:str) -> None: ...
#     def winner(self) -> str | None: ...
#     def available_moves(self) -> list[tuple[int,int]]: ...

class Player:
    """Base player type.

    Subclasses must implement next_move(board) -> (row, col).
    """
    def __init__(self, mark: str) -> None:
        assert mark in ("X", "O")
        self.mark = mark

    def next_move(self, board: "Board") -> Tuple[int, int]:
        raise NotImplementedError


@dataclass
class HumanPlayer(Player):
    """Human player. By default it reads from input(), but you can inject
    a custom prompt function for testing or GUI.
    """
    mark: str
    prompt_func: Callable[[str], str] | None = None

    def __post_init__(self) -> None:
        if self.prompt_func is None:
            self.prompt_func = input

    def next_move(self, board: "Board") -> Tuple[int, int]:
        while True:
            raw = self.prompt_func(f"{self.mark} move (row col or row,col): ").replace(",", " ").strip()
            parts = [p for p in raw.split() if p]
            try:
                if len(parts) != 2:
                    raise ValueError
                r, c = int(parts[0]), int(parts[1])
                if not (0 <= r < board.size and 0 <= c < board.size):
                    print("Out of bounds. Use 0..{0} for both row and col.".format(board.size - 1))
                    continue
                if not board.is_empty(r, c):
                    print("Cell already taken. Try another.")
                    continue
                return r, c
            except Exception:
                print("Invalid input. Example: 1 2 or 1,2")


@dataclass
class AIPlayer(Player):
    """Simple heuristic AI that mirrors your original logic:
    1) If I can win now, do it.
    2) Else if opponent can win next, block.
    3) Else pick random available cell.

    You can later replace this with a pluggable Strategy interface or Minimax.
    """
    mark: str

    def next_move(self, board: "Board") -> Tuple[int, int]:
        me = self.mark
        opp = "O" if me == "X" else "X"

        # helpers to try a move temporarily
        def try_move(r: int, c: int, m: str) -> bool:
            original = board.grid[r][c]
            board.grid[r][c] = m
            win = (board.winner() == m)
            board.grid[r][c] = original
            return win

        # 1) win if possible
        for (r, c) in board.available_moves():
            if try_move(r, c, me):
                return r, c

        # 2) block opponent
        for (r, c) in board.available_moves():
            if try_move(r, c, opp):
                return r, c

        # 3) otherwise random
        return random.choice(board.available_moves())
