# COMP 1510 Term Project Starter

Starter material for the COMP 1510 term project ("Build me an arcade!"). Read the
project handout first. This repository is not your submission.

## What is here

- `example_game.py`: a small, complete game that follows the contract. It defines
  `play(player_name)`, runs one full session, and returns the score. Load it into
  your shell while you develop. Every game you write follows this shape.
- `examples.py`: deliberately thin reference code. It shows the two things worth
  seeing once: reading the scoreboard file safely when it is missing or broken,
  and loading a game module by name. The arcade shell itself, the menu loop, the
  score recording, the display, is your design work.
- `test_examples.py`: three tiny pytest cases showing the shape of a test (plain
  asserts, one `pytest.raises`). Run `python3 -m pytest` to see them pass, then
  write your own.

## The contract

One line: a game module defines `play(player_name)`, runs exactly one session,
and returns the score as a number. The shell saves the score, so games never
touch the scoreboard file themselves.
