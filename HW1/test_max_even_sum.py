import pytest
from max_even_sum import max_even_sum

class TestMaxEvenSum:
    def test_empty_list(self):
        assert max_even_sum("") == 0
    
    def test_single_element(self):
        assert max_even_sum("1") == 0
        assert max_even_sum("2") == 2
    
    def test_even_sum(self):
        assert max_even_sum("1 2 3 4") == 10
        assert max_even_sum("1 2 3 4 3 1") == 14
    
    def test_odd_sum(self):
        assert max_even_sum("3 2 2 1 1") == 8
        assert max_even_sum("1 2 3 4 5") == 14
