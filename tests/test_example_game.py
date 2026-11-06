"""Tests for the example game's pure rule and scoring functions.

The impure edges need no tests: make_secret uses randomness, and
get_guess and check_guess read input and print.
"""

from example_game import judge_guess, score_for_attempt


def test_judge_guess_correct():
    """Test that a guess equal to the secret is judged correct."""
    assert judge_guess(7, 7) == "correct"


def test_judge_guess_low():
    """Test that a guess below the secret is judged low."""
    assert judge_guess(3, 7) == "low"


def test_judge_guess_high():
    """Test that a guess above the secret is judged high."""
    assert judge_guess(9, 7) == "high"


def test_score_for_attempt_first_guess_is_top_score():
    """Test the top score: a correct first guess."""
    assert score_for_attempt(1) == 50


def test_score_for_attempt_last_guess_is_floor_score():
    """Test the floor score: a correct guess on the last attempt."""
    assert score_for_attempt(5) == 10
