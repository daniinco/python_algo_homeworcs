import pytest
from validate import validate

def test_validate():
    assert validate([1, 2, 3, 4, 5], [1, 3, 5, 4, 2]) == True
    assert validate([1, 2, 3], [3, 1, 2]) == False
    assert validate([], []) == True
    assert validate([3, 2, 1], [1, 2, 3]) == True
    assert validate([1], [1]) == True
    assert validate([3, 1, 2], [1, 2, 3]) == True
    assert validate([1, 2, 3, 4], [3, 4, 1, 2]) == False