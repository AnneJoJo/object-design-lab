# Tic Tac Toe (OOP Python Version)

This project is an object-oriented implementation of Tic-Tac-Toe in Python. It supports human vs. computer play with multiple AI strategies (Minimax and Heuristic).

## Features

* **Clear OOP architecture**: Board, Player, Strategy, Renderer, and Game orchestrator are separated with well-defined responsibilities.
* **Multiple AI strategies**:

  * `MinimaxStrategy` — Optimal play, never loses.
  * `HeuristicStrategy` — Preserves the original logic: win if possible, block opponent, otherwise random.
* **Extensibility**: Easy to replace the renderer (CLI → GUI/Web) or add new strategies.
* **Testability**: Game logic is decoupled from I/O, making it straightforward to write unit tests.

## Project Structure

```
project_root/
│
├── game.py              # Main entry point, game loop orchestration
├── board.py             # Board logic (Board/Mark/GameResult/Move)
├── players.py           # Player abstraction: HumanPlayer, AIPlayer
├── strategies.py        # Strategy implementations: MinimaxStrategy, HeuristicStrategy
├── renderer.py          # Renderer abstraction and CLI implementation
└── README.md            # Project documentation (this file)
```

## Usage

1. Run `python game.py`
2. Choose your mark (X/O)
3. Decide whether to go first
4. Enter your moves as coordinates, e.g., `1 2` or `1,2`
5. After the game ends, choose whether to play again

## Example

```
Welcome to Tic Tac Toe! (rows/cols range 0–2)
Choose your mark (X/O): X
Use simple AI (win/block/random)? (Y/N): y
Do you want to go first? (Y/N): y
   0 1 2
0   | | 
   -----
1   | | 
   -----
2   | | 
X move (row col or row,col): 1 1
```

## Roadmap

* Add GUI renderer (pygame / PyQt)
* Extend to larger boards (4x4, Gomoku)
* Provide unit test examples
* Add logging and match replay functionality
