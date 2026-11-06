"""Scoreboard functions for the COMP 1510 term project.

Write load_scoreboard and save_scoreboard so the arcade keeps scores across
restarts. Their docstrings and the tests in tests/test_scoreboard.py define
the required behavior.
"""


def load_scoreboard(filename):
    """Return the scoreboard read from filename, or an empty one.

    :param filename: name of a JSON scoreboard file
    :return: the scoreboard as a dictionary. The caller still checks the
             nested record shape, as the README describes
    """
    # TODO: open filename, read it as JSON, and return a dictionary.
    # Start with an empty dictionary and print a friendly message when the
    # file is missing, is not valid JSON, or does not hold a dictionary.
    raise NotImplementedError("load_scoreboard is yours to write")


def save_scoreboard(scoreboard, filename):
    """Write the scoreboard to filename as JSON.

    :param scoreboard: the scoreboard dictionary to write
    :param filename: name of the JSON scoreboard file
    :return: None
    """
    # TODO: open filename for writing and save scoreboard as JSON.
    raise NotImplementedError("save_scoreboard is yours to write")
