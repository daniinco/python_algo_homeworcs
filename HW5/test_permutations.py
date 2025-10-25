from permutations import permutations

def test_permutations():
    assert permutations([]) == [[]]
    assert permutations([1]) == [[1]]
    
    list_of_permutations = permutations([1, 2, 3])
    assert len(list_of_permutations) == 6
    perm_set = set(map(tuple, list_of_permutations))
    assert (1, 2, 3) in perm_set
    assert (1, 3, 2) in perm_set
    assert (2, 1, 3) in perm_set
    assert (2, 3, 1) in perm_set
    assert (3, 1, 2) in perm_set
    assert (3, 2, 1) in perm_set

    list_of_permutations = permutations([1, 2, 3, 4])
    assert len(list_of_permutations) == 24
    for i in range(24):
        assert list_of_permutations[i] not in list_of_permutations[:i]
        assert list_of_permutations[i] not in list_of_permutations[i+1:]

    list_of_permutations = permutations([1, 2, 3, 4, 5, 6])
    assert len(list_of_permutations) == 720
    for i in range(720):
        assert list_of_permutations[i] not in list_of_permutations[:i]
        assert list_of_permutations[i] not in list_of_permutations[i+1:]