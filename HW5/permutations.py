from tracer import tracer

@tracer
def permutations(lst: list) -> list:
    """
    Возвращает список всех перестановок списка lst
    
    Args:
        lst: Список, для которого нужно найти все перестановки
        
    Returns:
        list: Список всех перестановок списка lst
    """
    if len(lst) <= 1:
        return [lst]
    else:
        result = []
        for i in range(len(lst)):
            lst[i], lst[-1] = lst[-1], lst[i]
            res_i = permutations(lst[:-1])
            for perm in res_i:
                perm.append(lst[-1])
                result.append(perm)
            lst[i], lst[-1] = lst[-1], lst[i]
        return result