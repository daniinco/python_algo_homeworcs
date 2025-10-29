from typing import List, Optional

def mergesort(nums: List[float], additional_memory: Optional[List[float]] = None, start_: int = 0, end_: int = None) -> List[float]:
    """
    Сортировка слиянием. Inplace
    Args:
        nums: Список чисел.
        additional_memory: Дополнительная память.
        start_: Начало сортировки.
        end_: Конец сортировки.
    Returns:
        List[float]: Отсортированный список.
    """
    if additional_memory is None:
        additional_memory = [0] * len(nums)
    if end_ is None:
        end_ = len(nums)
    if start_ != end_ - 1:
        mergesort(nums, additional_memory, start_, (start_ + end_) // 2)
        mergesort(nums, additional_memory, (start_ + end_) // 2, end_)
    else:
        return
    left_pointer = start_
    right_pointer = (start_ + end_) // 2
    for i in range(start_, end_):
        if left_pointer < (start_ + end_) // 2 and right_pointer < end_ and nums[left_pointer] < nums[right_pointer]:
            additional_memory[i] = nums[left_pointer]
            left_pointer += 1
        elif right_pointer >= end_:
            additional_memory[i] = nums[left_pointer]
            left_pointer += 1
        else:
            additional_memory[i] = nums[right_pointer]
            right_pointer += 1
    for i in range(start_, end_):
        nums[i] = additional_memory[i]

def quicksort(nums: List[float], start_: int = 0, end_: int = None) -> List[float]:
    """
    Быстрая сортировка. Inplace
    Args:
        nums: Список чисел.
        start_: Начало сортировки.
        end_: Конец сортировки.
    Returns:
        List[float]: Отсортированный список.
    """
    if len(nums) <= 1:
        return nums
    if end_ is None:
        end_ = len(nums)
    pivot = nums[start_]
    pivot_pointer = start_
    right_pointer = pivot_pointer + 1
    while right_pointer - pivot_pointer == 1 and right_pointer < end_:
        if nums[right_pointer] < pivot:
            nums[pivot_pointer], nums[right_pointer] = nums[right_pointer], nums[pivot_pointer]
            right_pointer += 1
            pivot_pointer += 1
        else:
            right_pointer += 1
    while right_pointer < end_:
        if nums[right_pointer] < pivot:
            nums[pivot_pointer], nums[right_pointer], nums[pivot_pointer + 1] = nums[right_pointer], nums[pivot_pointer + 1], nums[pivot_pointer]
            right_pointer += 1
            pivot_pointer += 1
        else:
            right_pointer += 1
    if pivot_pointer - start_ > 1:
        quicksort(nums, start_, pivot_pointer)
    if end_ - pivot_pointer > 2:
        quicksort(nums, pivot_pointer + 1, end_)
        