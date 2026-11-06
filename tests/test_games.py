"""Test the supplied game-module loader.

Run it with: python3 -m pytest
"""

import pytest

from games import load_game


def test_load_game_raises_for_missing_module():
    """Test that load_game raises ImportError for a missing module."""
    with pytest.raises(ImportError):
        load_game("no_such_game_module")
