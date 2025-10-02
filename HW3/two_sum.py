def two_sum(nums: list[int], k: int) -> list[int]:
    """
    Возвращает индексы двух чисел в массиве nums, сумма которых равна k.

    Args:
        nums: Массив чисел.
        k: Целевая сумма.
    
    Returns:
        Индексы двух чисел в массиве nums, сумма которых равна k.
    """
    numbers = {}
    for id, num in enumerate(nums):
        if k - num in numbers:
            return [numbers[k - num], id]
        numbers[num] = id
    return -1