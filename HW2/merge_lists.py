from typing import Iterable

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
    
    def __iter__(self) -> Iterable[float]:
        """
        Возвращает итератор по списку. Это нужно для тестов. Итератор возвращает значения узлов начиная с этого.
        Вообще мне не нравится этот метод.
        Я бы лучше реализовал тесты итерацией по самому двусвязному списку.
        Но в условии написано "Вернуть необходимо голову объединенного списка.", а не сам обьединенный список.
        Поэтому я реализовал итерацию по узлам для узла.

        Returns:
            Итератор по списку.
        """
        node = self
        while node is not None and node.value < float('inf'):
            yield node.value
            node = node.next

class ConnectedList:
    """
    Класс двусвязного списка без фиктивного элемента.
    """
    
    def __init__(self, init_list: Iterable[float] = ()) -> None:
        """
        Инициализация двусвязного списка.
        """

        self.start = None
        self.end = None
        self.length = 0
        for num in init_list:
            node = _Node(num)
            node.prev = self.end
            if self.start is None:
                self.start = node
            else:
                self.end.next = node
            self.end = node
            self.length += 1
    
    def append(self, value: float) -> None:
        """
        Добавляет узел в конец списка.
        Args:
            value: Значение узла.
        """
        node = _Node(value)
        node.prev = self.end
        if self.start is None:
            self.start = node
        else:
            self.end.next = node
        self.end = node
        self.length += 1
    
    def __len__(self) -> int:
        """
        Возвращает длину списка.
        Returns:
            Длина списка.
        """
        return self.length
    
    def __iter__(self) -> Iterable[float]:
        """
        Возвращает итератор по списку.
        Returns:
            Итератор по списку.
        """
        node = self.start
        while node is not None:
            yield node.value
            node = node.next


class ConnectedListWithFictive(ConnectedList):
    """
    Класс двусвязного списка с фиктивным узлом.
    """
    def __init__(self, init_list: Iterable[float] = ()) -> None:
        """
        Инициализация двусвязного списка.
        """
        super().__init__(init_list)
        last_node = _Node(float("inf"))
        last_node.prev = self.end
        if self.end is not None:
            self.end.next = last_node
        else:
            self.start = last_node
        self.end = last_node
    
    def append(self, value: float) -> None:
        """
        Добавляет узел в конец списка.
        Args:
            value: Значение узла.
        """
        new_node = _Node(value)
        new_node.prev = self.end.prev
        if self.end.prev is not None:
            self.end.prev.next = new_node
        else:
            self.start = new_node
        new_node.next = self.end
        self.end.prev = new_node
        self.length += 1
    
    def __iter__(self) -> Iterable[float]:
        """
        Возвращает итератор по списку.
        Returns:
            Итератор по списку.
        """
        node = self.start
        while node.value < float("inf"):
            yield node.value
            node = node.next


def merge_lists(list1: ConnectedList, list2: ConnectedList) -> _Node:
    """
    Объединяет два списка в один.
    Args:
        list1: Первый список.
        list2: Второй список.

    Returns:
        Объединенный список.
    """

    list1_pointer = list1.start
    list2_pointer = list2.start
    res_list = ConnectedList()
    for _ in range(len(list1) + len(list2)):
        if list1_pointer is None:
            res_list.append(list2_pointer.value)
            list2_pointer = list2_pointer.next
        elif list2_pointer is None:
            res_list.append(list1_pointer.value)
            list1_pointer = list1_pointer.next
        else:
            if list1_pointer.value < list2_pointer.value:
                res_list.append(list1_pointer.value)
                list1_pointer = list1_pointer.next
            else:
                res_list.append(list2_pointer.value)
                list2_pointer = list2_pointer.next
    return res_list.start

def merge_lists_with_fictive(list1: ConnectedListWithFictive, list2: ConnectedListWithFictive) -> _Node:
    """
    Объединяет два списка в один.
    Args:
        list1: Первый список.
        list2: Второй список.

    Returns:
        Объединенный список.
    """

    list1_pointer = list1.start
    list2_pointer = list2.start
    res_list = ConnectedListWithFictive()
    for _ in range(len(list1) + len(list2)):
        if list1_pointer.value < list2_pointer.value:
            res_list.append(list1_pointer.value)
            list1_pointer = list1_pointer.next
        else:
            res_list.append(list2_pointer.value)
            list2_pointer = list2_pointer.next
    return res_list.start