class _Node:
    """
    Класс узла двусвязного списка.
    """

    def __init__(self, value) -> None:
        """
        Args:
            value: Значение узла.
        """
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    """
    Класс очереди.
    """

    def __init__(self) -> None:
        """
        Инициализация очереди.
        """
        self.head = None
        self.tail = None
        self._length = 0
    
    def push(self, value: float) -> None:
        """
        Добавляет новый узел в конец очереди.

        Args:
            value: Значение нового узла.
        """

        node = _Node(value)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        self._length += 1
    
    def pop(self) -> float:
        """
        Удаляет первый узел из очереди.

        Returns:
            Значение первого элемента в очереди.
        """

        if self.head is None:
            raise IndexError("pop from empty queue")
        self._length -= 1
        node = self.head
        self.head = node.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return node.value
    
    def __len__(self) -> int:
        """
        Возвращает длину очереди.

        Returns:
            Длина очереди.
        """
        return self._length

class Stack:
    """
    Класс стека.
    """

    def __init__(self) -> None:
        """
        Инициализация стека.
        """
        self.tail = None
        self._length = 0
    
    def push(self, value: float) -> None:
        """
        Добавляет новый узел в стек.

        Args:
            value: Значение нового узла.
        """
        node = _Node(value)
        node.prev = self.tail
        self.tail = node
        self._length += 1
    
    def pop(self) -> float:
        """
        Удаляет последний узел из стека и возвращает его значение.

        Returns:
            Значение последнего узла в стеке.
        """

        if self.tail is None:
            raise IndexError("pop from empty stack")
        self._length -= 1
        node = self.tail
        self.tail = node.prev
        return node.value
    
    def peek(self) -> float:
        """
        Возвращает значение последнего узла в стеке.

        Returns:
            Значение последнего узла в стеке.
        """
        if self.tail is None:
            raise IndexError("peek from empty stack")
        return self.tail.value
    
    def __len__(self) -> int:
        """
        Возвращает длину стека.

        Returns:
            Длина стека.
        """
        return self._length
