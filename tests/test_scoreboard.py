"""The scoreboard tests are the specification for the stubs.

They fail until you implement load_scoreboard and save_scoreboard. Run them
with: python3 -m pytest
"""

from scoreboard import load_scoreboard, save_scoreboard


def test_load_scoreboard_round_trip(tmp_path):
    """Test that a saved scoreboard loads back with the same data.

    tmp_path is a fresh temporary folder pytest gives each test, so the
    test never writes into the real project folder.
    """
    target = tmp_path / "board.json"
    scoreboard = {"example_game": [{"player": "Sam", "score": 40}]}
    save_scoreboard(scoreboard, str(target))
    assert load_scoreboard(str(target)) == scoreboard


def test_load_scoreboard_survives_a_broken_file(tmp_path):
    """Test that a malformed scoreboard file comes back as an empty dict."""
    target = tmp_path / "broken.json"
    target.write_text("{not json at all")
    assert load_scoreboard(str(target)) == {}
