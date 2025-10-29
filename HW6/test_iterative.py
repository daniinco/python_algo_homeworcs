import time
from iterative import mergesort, quicksort
import sys
import random

def time_calculator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
        return result
    return wrapper

mergesort = time_calculator(mergesort)
quicksort = time_calculator(quicksort)

def test_sorts():
    nums = [1]
    mergesort(nums)
    assert nums == [1]
    nums = [1]
    quicksort(nums)
    assert nums == [1]
    nums = [5, 4, 3, 2, 1]
    mergesort(nums)
    assert nums == [1, 2, 3, 4, 5]
    nums = [5, 4, 3, 2, 1]
    quicksort(nums)
    assert nums == [1, 2, 3, 4, 5]
    nums = [5, 4, 3, 6, 2, 1]
    mergesort(nums)
    assert nums == [1, 2, 3, 4, 5, 6]
    nums = [5, 4, 3, 6, 2, 1]
    quicksort(nums)
    assert nums == [1, 2, 3, 4, 5, 6]
    for i in range(20):
        nums = list(range(1, 35))
        random.shuffle(nums)
        mergesort(nums)
        assert nums == list(range(1, 35))
        nums = list(range(1, 35))
        random.shuffle(nums)
        quicksort(nums)
        assert nums == list(range(1, 35))

def test_time():
    nums = list(range(10000, 0, -1))
    mergesort(nums)
    assert nums == list(range(1, 10001))
    nums = list(range(10000, 0, -1))
    quicksort(nums)
    assert nums == list(range(1, 10001))