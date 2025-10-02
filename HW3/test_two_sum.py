import pytest
from two_sum import two_sum

def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 4, 8], 12) == [1, 2]
    assert two_sum([0, 4, 3], 3) == [0, 2]
    assert two_sum([-8, 4, 3, 43, 8], 0) == [0, 4]