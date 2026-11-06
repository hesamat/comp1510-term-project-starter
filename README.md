# COMP 1510 Term Project Starter

Starter material for the COMP 1510 term project ("Build me an arcade!"). Read the
project handout first. This repository is not your submission: press **Use this
template** to create your own private repository from it, then clone that
repository. Replace this README with your own when you build your arcade.

## What is here

- `game.py`: the menu skeleton. It shows the menu, calls a game's
  `play(player_name)`, records the returned score in memory, and shows each game's
  top score. It does not save scores yet; the `TODO` comments mark where to add
  `scoreboard.json` loading, saving, and wrong-shape handling. Run it with
  `python3 game.py`.
- `example_game.py`: a small, complete game that follows the contract. It is already
  in the skeleton's `GAMES` list, so you can run the arcade immediately.
- `scoreboard.py`: the scoreboard functions you write. Fill in
  `load_scoreboard` and `save_scoreboard` so scores survive a restart. Their
  docstrings and the tests in `tests/test_scoreboard.py` define the required
  behavior.
- `games.py`: the supplied module loader. `load_game` imports a game module by
  name; the course does not cover `importlib`, so treat this file as supplied
  machinery and leave it alone.
- `tests/`: `conftest.py` puts the project on the import path.
  `test_scoreboard.py` is the specification for the scoreboard stubs.
  `test_games.py` checks the supplied loader. `test_example_game.py` tests the
  example game's pure rule functions.
- `.gitignore`: already ignores `scoreboard.json`, `arcade.bundle`, and the
  cache folders Python, PyCharm, and pytest generate.
- `ARCADE_PLAN.md`: the plan template. Draft your plan here, then turn it into
  one PDF named `arcade-plan.pdf`: paste the markdown into a browser converter
  such as dillinger.io and export, or export from a markdown editor like VS
  Code. Commit it by November 13.
- `example-plan.md` and `example-plan.pdf`: a filled-in example of the plan,
  using the supplied example game. Your plan covers your two chosen games
  instead.

## The contract

A game module defines `play(player_name)`, runs exactly one session, and returns the
score as a nonnegative `int`, where higher is better. The menu is responsible for
saving the score, so games never touch the scoreboard file themselves.

## Your two required games

Pick two games from the handout, with at least one of them medium or spicy. Add each
module name to `GAMES` in `game.py` and add the module file to the project. A third
game is optional bonus. The example game does not count toward the two.

## The scoreboard

`game.py` records scores in memory using this shape:

```json
{
  "example_game": [
    {"player": "Sam", "score": 40},
    {"player": "Ada", "score": 30}
  ]
}
```

Your job is to make the scores survive a restart:

- load `scoreboard.json` at startup, starting fresh if it is missing, malformed,
  or not in the expected shape.
- save it after every game.

`scoreboard.py` has stubs for `load_scoreboard` and `save_scoreboard`, with
docstrings and TODO comments. You write both functions. The two scoreboard tests
in `tests/test_scoreboard.py` are the specification: make them pass. You still
need to check the nested shape yourself: valid JSON is not necessarily a valid
scoreboard. You may keep this layout or design your own. If you change it, update
`show_scoreboard` and document the new shape in your README. The included
`.gitignore` already ignores `scoreboard.json` and `arcade.bundle`.

## Run it

**PyCharm:** accept the virtual environment PyCharm offers when you open the
project, and install `pytest` from the **Python Packages** panel. Then run
`game.py` to play, and right-click the `tests` folder to run the tests.

**Terminal:** from the top-level folder, set up once:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest
```

Then `python game.py` plays and `python -m pytest` runs the tests. The two
scoreboard tests in `test_scoreboard.py` fail until you implement the stubs; the
rest should pass. In a new terminal, run the `activate` line again first.

Read every line of `game.py` you keep. You must be able to explain it in the live
demonstration.
