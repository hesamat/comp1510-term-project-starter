"""Supplied game-module loader for the COMP 1510 term project.

load_game imports a game module by name. The course does not cover importlib,
so treat this file as supplied machinery and leave it as is.
"""

import importlib


def load_game(module_name):
    """Return a game module given its module name.

    :param module_name: the module's name as a string, like "example_game"
    :return: the loaded module object
    """
    return importlib.import_module(module_name)
