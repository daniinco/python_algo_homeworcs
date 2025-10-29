from typing import List

def quickselect(nums: List[float], k: int) -> float:
    """
    Выбор k-ой порядковой статистики.
    Args:
        nums: Список чисел.
        k: k-ая порядковая статистика.
    Returns:
        float: k-ая порядковая статистика.
    """
    k = len(nums) - k
    start_, end_ = 0, len(nums)
    nums = nums[:]
    while end_ - start_ > 1:
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
        if pivot_pointer == k:
            return nums[k]
        elif pivot_pointer > k:
            end_ = pivot_pointer
        elif pivot_pointer < k:
            start_ = pivot_pointer + 1
    return nums[k]
