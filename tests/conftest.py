"""Put the project folder on sys.path so the tests can import the modules.

pytest imports conftest.py before collecting the sibling test files, so
the insertion below is in place by the time the tests run their imports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
