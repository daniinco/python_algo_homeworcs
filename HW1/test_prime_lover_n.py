import pytest
from prime_lower_n import prime_lower_n

class TestPrimeLoverN:
    def test_nums(self):
        assert prime_lower_n(1) == 0
        assert prime_lower_n(2) == 0
        assert prime_lower_n(3) == 1
        assert prime_lower_n(4) == 2
        assert prime_lower_n(-5) == 0
        assert prime_lower_n(10) == 4
        assert prime_lower_n(100) == 25
        assert prime_lower_n(7) == 3
