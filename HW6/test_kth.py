from kth import quickselect
import random

def test_kth():
    nums = [1, 2, 3, 4, 5, 6]
    assert quickselect(nums, 1) == 6
    nums = [3, 2, 1, 5, 6, 4]
    assert quickselect(nums, 2) == 5
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    assert quickselect(nums, 4) == 4
    nums = [3, 3, 3, 4, 4, 4]
    assert quickselect(nums, 3) == 4
    n = 35
    for i in range(20):
        nums = list(range(1, n + 1))
        random.shuffle(nums)
        for j in range(n, 0, -1):
            assert quickselect(nums, j) == n - j + 1
