import pytest
from palindrome import is_palindrome

class TestPalindrome:
    def test_single_digit(self):
        assert is_palindrome(1) == True
        assert is_palindrome(2) == True
        assert is_palindrome(9) == True
    
    def test_non_polimdromes(self):
        assert is_palindrome(10) == False
        assert is_palindrome(133) == False
    
    def test_polimdromes(self):
        assert is_palindrome(121) == True
        assert is_palindrome(11) == True
        assert is_palindrome(12321) == True
        assert is_palindrome(45666654) == True
