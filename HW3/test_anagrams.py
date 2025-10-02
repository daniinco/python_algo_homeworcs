import pytest
from anagrams import group_anagrams
import random
import string

def generate_random_string():
    return ''.join(random.choices(string.ascii_letters, k=5))

def test_group_anagrams():
    groups = [set(group) for group in group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])]
    for group in [{"eat", "tea", "ate"}, {"bat"}, {"tan", "nat"}]:
        assert group in groups
    
    groups = [set(group) for group in group_anagrams(["aab", "baa", "abb", "bba"])]
    for group in [{"aab", "baa"}, {"abb", "bba"}]:
        assert group in groups
    
    assert len(group_anagrams([])) == 0

    assert group_anagrams(["a"]) == [["a"]]

    groups = [set(group) for group in group_anagrams(["aab", "baa", "abb", "bba", "aabb", "baab"])]
    for group in [{"aab", "baa"}, {"abb", "bba"}, {"aabb", "baab"}]:
        assert group in groups
    
    for i in range(10000):
        word = generate_random_string()
        groups = [set(group) for group in group_anagrams(["aaaaa", word])]
        for group in [{"aaaaa"}, {word}]:
            assert group in groups