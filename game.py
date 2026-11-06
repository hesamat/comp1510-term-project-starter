"""The arcade menu skeleton for the COMP 1510 term project.

This file is a working starting point. It shows the menu, calls a game's
play(player_name), records the returned score in memory, and shows each
game's top score.

It does not save scores yet. Loading and saving scoreboard.json, and
detecting a file in the wrong shape, are yours to add. The TODO comments
mark both places. scoreboard.py has stubs for the file handling; games.py
supplies load_game.

Add your own game modules to GAMES. Read every line you keep: you must be
able to explain it in the live demonstration.

In-memory scoreboard format:
{
    "example_game": [
        {"player": "Sam", "score": 40},
        {"player": "Ada", "score": 30}
    ]
}
"""

from games import load_game

# TODO: from scoreboard import load_scoreboard, save_scoreboard

GAMES = ("example_game",)


def game_title(module_name):
    """Return a display name for a game module.

    :param module_name: the module's name, like "example_game"
    :return: the name with underscores replaced by spaces and title case
    """
    return module_name.replace("_", " ").title()


def show_menu():
    """Print the arcade menu.

    :return: None
    """
    print("\n=== The Arcade ===")
    for index in range(len(GAMES)):
        print(f"{index + 1}. {game_title(GAMES[index])}")
    print(f"{len(GAMES) + 1}. Show scoreboard")
    print(f"{len(GAMES) + 2}. Quit")


def choose_game(choice):
    """Return the module name for a menu choice, or None for an invalid choice.

    :param choice: the player's menu input
    :return: the chosen module name, or None when the choice is not a game
    """
    if not choice.isdecimal():
        return None
    number = int(choice)
    if 1 <= number <= len(GAMES):
        return GAMES[number - 1]
    return None


def record_score(scoreboard, player_name, module_name, score):
    """Add one finished game's score to the scoreboard.

    :param scoreboard: the scoreboard dictionary
    :param player_name: the player's name
    :param module_name: the game module's name
    :param score: the score the game returned
    :return: None
    """
    if module_name not in scoreboard:
        scoreboard[module_name] = []
    scoreboard[module_name].append({"player": player_name, "score": score})


def best_record(records):
    """Return the highest-scoring record, or None when records is empty.

    :param records: a list of {"player": ..., "score": ...} records
    :return: the record with the highest score, or None for an empty list
    """
    if not records:
        return None
    best = records[0]
    for record in records[1:]:
        if record["score"] > best["score"]:
            best = record
    return best


def show_scoreboard(scoreboard):
    """Print each game's top score and who set it.

    :param scoreboard: the scoreboard dictionary
    :return: None
    """
    print("\n=== Scoreboard ===")
    for module_name in GAMES:
        best = best_record(scoreboard.get(module_name, []))
        if best is None:
            print(f"{game_title(module_name)}: no scores yet")
        else:
            print(f"{game_title(module_name)}: {best['player']} "
                  f"with {best['score']}")


def play_game(scoreboard, player_name, module_name):
    """Play one game and record its score in memory.

    :param scoreboard: the scoreboard dictionary
    :param player_name: the player's name
    :param module_name: the game module's name
    :return: None
    """
    try:
        game = load_game(module_name)
    except ImportError:
        print(f"Could not load {game_title(module_name)}.")
        return
    score = game.play(player_name)
    record_score(scoreboard, player_name, module_name, score)
    # TODO: save scoreboard to scoreboard.json here.
    print(f"Score recorded: {score}")


def main():
    """Run the arcade menu until the player quits."""
    print("Welcome to the arcade!")
    player_name = input("Your name: ").strip()
    while not player_name:
        player_name = input("Please enter a name: ").strip()

    # TODO: load scoreboard.json here. Start fresh if it is missing,
    # malformed, or not in the expected shape.
    scoreboard = {}
    while True:
        show_menu()
        choice = input("Choose: ").strip()
        if choice == str(len(GAMES) + 1):
            show_scoreboard(scoreboard)
        elif choice == str(len(GAMES) + 2):
            print("Thanks for playing!")
            break
        else:
            module_name = choose_game(choice)
            if module_name is None:
                print("Please choose a number from the menu.")
            else:
                play_game(scoreboard, player_name, module_name)


if __name__ == "__main__":
    main()
