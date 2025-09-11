def prime_lower_n(n: int) -> int:
    """
    Находит сколько есть простых чисел меньших n
    ассимптотика n * n / log(n)
    
    Args:
        n: Число
        
    Returns:
        Сколько есть простых чисел меньших n
    """
    if n < 3:
        return 0
    prime_count = 0
    prime_flags =[0] * n
    for num in range(2, n):
        if prime_flags[num] == 0:
            prime_count += 1
            for comp_num in range(num, n, num):
                prime_flags[comp_num] = 1
    return prime_count
