"""Reference examples for the COMP 1510 term project.

This file is deliberately thin. It shows the two things worth seeing once:
reading the scoreboard file safely, and loading a game module by name.
Everything else, the menu loop, the score recording, the display, is your
design work. Copy what helps, understand every line you keep.
"""

import importlib
import json


def load_scoreboard(filename):
    """Return the scoreboard read from filename, or an empty one.

    :param filename: name of a JSON scoreboard file
    :postcondition: never raise for a missing or malformed file
    :return: the scoreboard as a dictionary, empty if the file is unusable
    """
    try:
        with open(filename) as scoreboard_file:
            data = json.load(scoreboard_file)
        if isinstance(data, dict):
            return data
        print("The scoreboard file is not in the expected shape.")
        return {}
    except FileNotFoundError:
        print("No scoreboard yet. Starting a fresh one.")
        return {}
    except json.JSONDecodeError:
        print("The scoreboard file is damaged. Starting a fresh one.")
        return {}


def save_scoreboard(filename, scoreboard):
    """Write the scoreboard to filename as JSON.

    :param filename: name of the JSON scoreboard file
    :param scoreboard: the scoreboard dictionary to write
    :postcondition: filename contains scoreboard in JSON form
    """
    with open(filename, "w") as scoreboard_file:
        json.dump(scoreboard, scoreboard_file, indent=2)


def load_game(module_name):
    """Return a game module given its module name.

    :param module_name: the module's name as a string, like "example_game"
    :precondition: a file named module_name.py exists and defines play
    :postcondition: import errors surface as ImportError from importlib
    :return: the loaded module object
    """
    return importlib.import_module(module_name)
