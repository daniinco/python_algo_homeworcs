from stack_and_queue import Stack

def validate(pushed: list[int], popped: list[int]) -> bool:
    """
    Проверяет, существует ли последовательность операций push и pop, которая соответствует последовательностям pushed и popped.

    Args:
        pushed: Последовательность элементов в порядке, в котором над элементами проводится операция push.
        popped: Последовательность элементов в порядке, в котором над элементами проводится операция pop.

    Returns:
        True, если можно получить popped из pushed, иначе False.
    """

    stack = Stack()
    curent_pop_id = 0
    for value in pushed:
        stack.push(value)
        while len(stack) > 0 and stack.peek() == popped[curent_pop_id]:
            stack.pop()
            curent_pop_id += 1
    if len(stack) == 0:
        return True
    return False