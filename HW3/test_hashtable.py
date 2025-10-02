import pytest
from hashtable import HashTable

def test_hashtable():
    table = HashTable()
    table["a"] = 1
    for i in range(1000):
        table[i] = i
    for i in range(1000):
        assert i in table
        assert table[i] == i
        del table[i]
        assert i not in table
    for i in range(1000):
        table[i] = i
    for i in range(1000):
        assert i in table
        assert table[i] == i
        del table[i]
        assert i not in table
    table["a"] = 1
    assert table["a"] == 1
    table["a"] = 2
    assert table["a"] == 2
    del table["a"]
    assert "a" not in table