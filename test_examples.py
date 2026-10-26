"""Three tiny pytest cases, to show the shape of a test.

Run them with: python3 -m pytest
The first two use plain asserts. The third uses pytest.raises, which the
course covers later, to check that the right exception is raised.
"""

import pytest

from examples import load_game, load_scoreboard, save_scoreboard


def test_load_scoreboard_round_trip(tmp_path):
    """Test that a saved scoreboard loads back with the same data.

    tmp_path is a fresh temporary folder pytest gives each test, so the
    test never writes into the real project folder.
    """
    target = tmp_path / "board.json"
    scoreboard = {"Sam": {"guess_the_number": [30, 40]}}
    save_scoreboard(str(target), scoreboard)
    assert load_scoreboard(str(target)) == scoreboard


def test_load_scoreboard_survives_a_broken_file(tmp_path):
    """Test that a malformed scoreboard file comes back as an empty dict."""
    target = tmp_path / "broken.json"
    target.write_text("{not json at all")
    assert load_scoreboard(str(target)) == {}


def test_load_game_raises_for_missing_module():
    """Test that load_game raises ImportError for a module that does not exist."""
    with pytest.raises(ImportError):
        load_game("no_such_game_module")
