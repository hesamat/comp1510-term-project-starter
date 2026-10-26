"""A complete example game for the COMP 1510 term project.

This file follows the contract exactly: it defines play(player_name), runs
exactly one session, and returns the score as a number. It never touches the
scoreboard file, because saving scores is the shell's job.

Copy this shape for every game you write. The session rules are yours to
design; the contract is not.
"""

import random

SECRET_LOW = 1
SECRET_HIGH = 20
MAX_GUESSES = 5


def make_secret():
    """Return the secret number for one session.

    :postcondition: the secret is between SECRET_LOW and SECRET_HIGH
    :return: the secret as an int
    """
    return random.randint(SECRET_LOW, SECRET_HIGH)


def get_guess(attempt, max_guesses):
    """Ask for a guess until the player enters a valid whole number.

    :param attempt: which guess this is, starting at 1
    :param max_guesses: how many guesses the player has in total
    :precondition: attempt and max_guesses are positive ints
    :postcondition: the returned value is an int between SECRET_LOW and SECRET_HIGH
    :return: the player's guess as an int
    """
    while True:
        raw = input(f"Guess {attempt} of {max_guesses}, enter a number "
                    f"({SECRET_LOW}-{SECRET_HIGH}): ")
        if raw.isdigit() and SECRET_LOW <= int(raw) <= SECRET_HIGH:
            return int(raw)
        print("That is not a number in range. Try again.")


def check_guess(guess, secret):
    """Compare a guess against the secret.

    :param guess: the player's guess as an int
    :param secret: the secret number as an int
    :postcondition: print one feedback line and no more
    :return: True if the guess is correct, else False
    """
    if guess == secret:
        print("You got it!")
        return True
    if guess < secret:
        print("Too low.")
    else:
        print("Too high.")
    return False


def play(player_name):
    """Run one full session of guess the number and return the score.

    :param player_name: the player's name as a string
    :precondition: player_name is a non-empty string
    :postcondition: the session ends with exactly one outcome
    :return: the session's score as an int
    """
    secret = make_secret()
    print(f"\n{player_name}, I am thinking of a number between "
          f"{SECRET_LOW} and {SECRET_HIGH}.")
    for attempt in range(1, MAX_GUESSES + 1):
        guess = get_guess(attempt, MAX_GUESSES)
        if check_guess(guess, secret):
            score = (MAX_GUESSES + 1 - attempt) * 10
            print(f"You scored {score} points with {attempt} guesses.")
            return score
    print(f"Out of guesses. The number was {secret}. You scored 0 points.")
    return 0
