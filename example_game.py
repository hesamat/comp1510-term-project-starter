"""A complete example game for the COMP 1510 term project.

This file follows the contract exactly: it defines play(player_name), runs
exactly one session, and returns the score as a number. It never touches the
scoreboard file, because saving scores is the menu's job.

The game's rules live in pure functions (judge_guess and score_for_attempt),
whose results depend only on their arguments. Input and printing stay at the
edges (get_guess and check_guess). Copy this shape for every game you write:
the session rules are yours to design, but the contract and the pure-rule
pattern are not.
"""

import random

SECRET_LOW = 1
SECRET_HIGH = 20
MAX_GUESSES = 5


def make_secret():
    """Return the secret number for one session.

    :return: the secret as an int
    """
    return random.randint(SECRET_LOW, SECRET_HIGH)


def judge_guess(guess, secret):
    """Return the verdict for one guess against the secret.

    :param guess: the player's guess as an int
    :param secret: the secret number as an int
    :return: "correct" when the guess matches the secret, "low" when the
             guess is smaller, and "high" when it is larger
    """
    if guess == secret:
        return "correct"
    if guess < secret:
        return "low"
    return "high"


def score_for_attempt(attempt):
    """Return the score earned by a correct guess on the given attempt.

    :param attempt: which guess this was, starting at 1
    :return: the score as a nonnegative int
    """
    return (MAX_GUESSES + 1 - attempt) * 10


def get_guess(attempt, max_guesses):
    """Ask for a guess until the player enters a valid whole number.

    :param attempt: which guess this is, starting at 1
    :param max_guesses: how many guesses the player has in total
    :return: the player's guess as an int
    """
    while True:
        raw = input(f"Guess {attempt} of {max_guesses}, enter a number "
                    f"({SECRET_LOW}-{SECRET_HIGH}): ").strip()
        if raw.isdecimal() and SECRET_LOW <= int(raw) <= SECRET_HIGH:
            return int(raw)
        print("That is not a number in range. Try again.")


def check_guess(guess, secret):
    """Print one feedback line for a guess and report whether it hit.

    :param guess: the player's guess as an int
    :param secret: the secret number as an int
    :return: True if the guess is correct, else False
    """
    verdict = judge_guess(guess, secret)
    if verdict == "correct":
        print("You got it!")
        return True
    if verdict == "low":
        print("Too low.")
    else:
        print("Too high.")
    return False


def play(player_name):
    """Run one full session of guess the number and return the score.

    :param player_name: the player's name as a string
    :return: the session's score as an int
    """
    secret = make_secret()
    print(f"\n{player_name}, I am thinking of a number between "
          f"{SECRET_LOW} and {SECRET_HIGH}.")
    for attempt in range(1, MAX_GUESSES + 1):
        guess = get_guess(attempt, MAX_GUESSES)
        if check_guess(guess, secret):
            score = score_for_attempt(attempt)
            print(f"You scored {score} points with {attempt} guesses.")
            return score
    print(f"Out of guesses. The number was {secret}. You scored 0 points.")
    return 0
