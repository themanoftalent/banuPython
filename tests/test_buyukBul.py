import os
import sys
import pytest

# Add the project root to sys.path so that buyukBul can be imported
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from buyukBul import find_max


def test_find_max():
    assert find_max([1, 3, 2]) == 3
    assert find_max([-1, 0, -10]) == 0
    assert find_max([7]) == 7
