from functools import wraps

def tracer(func: callable) -> callable:
    tracer_stage = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal tracer_stage
        print("  " * tracer_stage + f"Вызываем {func.__name__} с позиционными аргументами {args} и именованными аргументами {kwargs}")
        tracer_stage += 1
        res = func(*args, **kwargs)
        tracer_stage -= 1
        print("  " * tracer_stage + f"Возвращаем {res}")
        return res
    
    return wrapper

@tracer
def fibbonacci_luca(numbers_type: str, n: int) -> int:
    """
    Возвращает n-ое число Фибоначчи или Люка https://ru.wikipedia.org/wiki/Числа_Люка
    
    Args:
        numbers_type: Тип чисел fibbonacci или luca
        n: Номер числа Фибоначчи
        
    Returns:
        int: n-ое число Фибоначчи
    """
    if numbers_type == "fibbonacci":
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibbonacci_luca("fibbonacci", n-1) + fibbonacci_luca("fibbonacci", n-2)
    elif numbers_type == "luca":
        if n == 0:
            return 2
        elif n == 1:
            return 1
        else:
            return fibbonacci_luca("luca", n-1) + fibbonacci_luca("luca", n-2)