from typing import List
from collections import deque

def mergesort(nums: List[float]) -> List[float]:
    """
    Сортировка слиянием. Inplace. Итеративная
    Args:
        nums: Список чисел.
    Returns:
        List[float]: Отсортированный список.
    """
    k = 2
    additional_memory = [0] * len(nums)
    while k < len(nums) * 2:
        for i in range(0, len(nums), k):
            start_1 = i
            end_2 = min(start_1 + k, len(nums))
            if end_2 - start_1 <= k // 2:
                continue
            start_2 = start_1 + k // 2
            end_1 = start_2
            mem_pointer = start_1
            while start_2 < end_2 or start_1 < end_1:
                if start_1 >= end_1:
                    additional_memory[mem_pointer] = nums[start_2]
                    start_2 += 1
                    mem_pointer += 1
                elif start_2 >= end_2:
                    additional_memory[mem_pointer] = nums[start_1]
                    start_1 += 1
                    mem_pointer += 1
                elif nums[start_1] < nums[start_2]:
                    additional_memory[mem_pointer] = nums[start_1]
                    start_1 += 1
                    mem_pointer += 1
                else:
                    additional_memory[mem_pointer] = nums[start_2]
                    start_2 += 1
                    mem_pointer += 1
            for i in range(i, end_2):
                nums[i] = additional_memory[i]
        k *= 2


def quicksort(nums):
    """
    Быстрая сортировка. Inplace. Итеративная
    Args:
        nums: Список чисел.
    Returns:
        List[float]: Отсортированный список.
    """
    deq = deque([(0, len(nums))])
    while len(deq) > 0:
        start_, end_ = deq.pop()
        if end_ - start_ <= 1:
            continue
        pivot = nums[start_]
        pivot_pointer = start_
        right_pointer = pivot_pointer + 1
        while right_pointer - pivot_pointer == 1 and right_pointer < end_:
            if nums[right_pointer] < pivot:
                nums[pivot_pointer], nums[right_pointer] = nums[right_pointer], nums[pivot_pointer]
                pivot_pointer += 1
                right_pointer += 1
            else:
                right_pointer += 1
        while right_pointer < end_:
            if nums[right_pointer] < pivot:
                nums[pivot_pointer], nums[right_pointer], nums[pivot_pointer + 1] = nums[right_pointer], nums[pivot_pointer + 1], nums[pivot_pointer]
                pivot_pointer += 1
                right_pointer += 1
            else:
                right_pointer += 1
        if pivot_pointer - start_ > 1:
            deq.append((start_, pivot_pointer))
        if end_ - pivot_pointer > 2:
            deq.append((pivot_pointer + 1, end_))
