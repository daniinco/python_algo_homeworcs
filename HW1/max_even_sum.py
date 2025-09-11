def max_even_sum(num_string: str) -> int:
    """
    Находит максимальную сумму элементов массива, которая делится на 2.
    
    Args:
        num_string: Строка с числами
        
    Returns:
        Максимальная возможная четная сумма
    """
    nums = [int(x) for x in num_string.split()]
    sum_ = sum(nums)
    if sum_ % 2 == 0:
        return sum_
    previous_odd = 0
    for number in nums:
        if number % 2 == 1: # для нечетных чисел
            if sum_ % 2 == 1 or sum_ + previous_odd - number > sum_: #если это первое нечетное число или сумма без текущего числа больше
                sum_ += previous_odd - number
                previous_odd = number
    return sum_
