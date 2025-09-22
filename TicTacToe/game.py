# game.py
from typing import Tuple
from board import Board
from player import Player           # 你已有的 Player（只需有 .mark 即可）
from strategies import stretigic     # AI 类名按你说的写法
from renderer import render          # 你已经单独封装的渲染函数

def ask_yes_no(prompt: str) -> bool:
    s = input(prompt).strip().lower()
    return s.startswith("y")

def ask_mark(prompt: str = "Choose your mark (X/O): ") -> str:
    while True:
        m = input(prompt).strip().upper()
        if m in ("X", "O"):
            return m
        print("Please enter X or O.")

def human_move(board: Board) -> Tuple[int, int]:
    while True:
        raw = input("Your move (row col or row,col): ").replace(",", " ").strip()
        parts = [p for p in raw.split() if p]
        try:
            if len(parts) != 2:
                raise ValueError
            r, c = int(parts[0]), int(parts[1])
            if not (0 <= r < board.size and 0 <= c < board.size):
                print(f"Out of bounds. Use 0..{board.size-1}.")
                continue
            if not board.is_empty(r, c):
                print("Cell already taken. Try another.")
                continue
            return r, c
        except Exception:
            print("Invalid input. Example: 1 2 or 1,2")

def game_once() -> None:
    board = Board(size=3)

    # players
    human_mark = ask_mark()
    human = Player(human_mark)
    ai_mark = "O" if human.mark == "X" else "X"
    ai = stretigic(ai_mark)  # 按你的命名

    human_turn = ask_yes_no("Do you want to go first? (Y/N): ")

    # main loop
    while True:
        render(board)  # 外部渲染

        if human_turn:
            r, c = human_move(board)
            board.place(r, c, human.mark)
        else:
            r, c = ai.next_move(board)  # AI 负责给出坐标
            board.place(r, c, ai.mark)
            print(f"Computer plays: ({r}, {c})")

        w = board.winner()
        if w is not None:
            render(board)
            print("You win!" if w == human.mark else "Computer wins!")
            return

        if board.is_full():
            render(board)
            print("Draw!")
            return

        human_turn = not human_turn

def main() -> None:
    print("Welcome to Tic Tac Toe! (rows/cols range 0–2)")
    while True:
        game_once()
        if not ask_yes_no("Play again? (Y/N): "):
            print("Bye!")
            break

if __name__ == "__main__":
    main()
