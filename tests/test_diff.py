from gendiff.scripts.gendiff import main
import pytest


def test_reverse():
    assert main() is None
