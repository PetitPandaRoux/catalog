import pytest

def func(x):
    return x + 1

def test_myTest():
    assert func(3) == 5