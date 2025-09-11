def is_palindrome(x: int) -> bool:
    """
    Проверяет, является ли число палиндромом
    
    Args:
        x: Число
        
    Returns:
        True, если число является палиндромом иначе False
    """
    deg = 0
    pow_ = 1
    while pow_ <= x:
        deg += 1
        pow_ *= 10
    pow_ //= 10
    for i in range(deg  // 2):
        last_digit = x % 10
        first_digit = x // pow_
        if last_digit != first_digit:
            return False
        x = (x % pow_) // 10
        pow_ //= 100
    return True
