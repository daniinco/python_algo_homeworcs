from __future__ import annotations


class Node:
    """
    Класс узла дерева.
    """
    def __init__(self, value: float):
        """
        Инициализация узла.

        Args:
            value: Значение узла.
        """
        self.value = value
        self.left = None
        self.right = None
        self.father = None
        self.father_type = None

    def insert(self, value: float) -> None:
        """
        Вставка узла в дерево.

        Args:
            value: Значение узла.
        """
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
                self.left.father = self
                self.father_type = "left"
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
                self.right.father = self
                self.father_type = "right"
            else:
                self.right.insert(value)
    
    def min(self) -> Node:
        """
        Поиск минимального узла в дереве.

        Returns:
            Node: Минимальный узел.
        """
        if self.left is None:
            return self
        else:
            return self.left.min()
    
    def max(self) -> Node:
        """
        Поиск минимального узла в дереве.

        Returns:
            Node: Минимальный узел.
        """
        if self.right is None:
            return self
        else:
            return self.right.max()
    
    def pop(self, value: float) -> None:
        """
        Удаление узла из дерева.

        Args:
            value: Значение узла.
        """
        if value < self.value:
            if self.left is not None:
                self.left.pop(value)
            else:
                raise ValueError("Value not found")
        elif value > self.value:
            if self.right is not None:
                self.right.pop(value)
            else:
                raise ValueError("Value not found")
        else:
            if self.left is None and self.right is None:
                if self.father_type == "left":
                    self.father.left = None
                elif self.father_type == "right":
                    self.father.right = None
                else:
                    self.father = None
            elif self.left is None:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
            elif self.right is None:
                self.value = self.left.value
                self.left = self.left.left
                self.right = self.left.right
            else:
                min_node = self.right.min()
                self.value = min_node.value
                min_node.pop(min_node.value)
    
    def get_by_value(self, value: float) -> Node:
        """
        Поиск узла по значению.

        Args:
            value: Значение узла.
        Returns:
            Node: Узел.
        """
        if value < self.value:
            if self.left is not None:
                return self.left.get_by_value(value)
            else:
                raise ValueError("Value not found")
        elif value > self.value:
            if self.right is not None:
                return self.right.get_by_value(value)
            else:
                raise ValueError("Value not found")
        else:
            return self

class Tree:
    """
    Класс дерева.
    """
    def __init__(self):
        """
        Инициализация дерева.

        Args:
            value: Значение корневого узла.
        """
        self.root = None
    
    def add(self, value: float) -> None:
        """
        Вставка узла в дерево.

        Args:
            value: Значение узла.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insert(value)
    
    def pop(self, value: float) -> None:
        """
        Удаление узла из дерева.

        Args:
            value: Значение узла.
        """
        if self.root is not None:
            self.root.pop(value)
    
    def get_by_value(self, value: float) -> Node:
        """
        Поиск узла по значению.

        Args:
            value: Значение узла.
        Returns:
            Node: Узел.
        """
        if self.root is not None:
            return self.root.get_by_value(value)
        else:
            raise ValueError("Value not found")

def _preorder(node: Node, list_result: list[float]) -> list[float]:
    list_result.append(node.value)
    if node.left is not None:
        _preorder(node.left, list_result)
    if node.right is not None:
        _preorder(node.right, list_result)
    return list_result


def preorder(tree: Tree) -> None:
    """
    Обход дерева в прямом порядке.

    Args:
        node: Корень дерева.

    Returns:
        list[float]: Список значений узлов дерева в порядке обхода.
    """
    if tree.root is None:
        return []
    else:
        list_result = []
        _preorder(tree.root, list_result)
        return list_result

def _postorder(node: Node, list_result: list[float]) -> list[float]:
    if node.left is not None:
        _postorder(node.left, list_result)
    if node.right is not None:
        _postorder(node.right, list_result)
    list_result.append(node.value)
    return list_result

def postorder(tree: Tree) -> None:
    """
    Обход дерева в обратном порядке.

    Args:
        node: Корень дерева.

    Returns:
        list[float]: Список значений узлов дерева в порядке обхода.
    """
    if tree.root is None:
        return []
    else:
        list_result = []
        _postorder(tree.root, list_result)
        return list_result

def _inorder(node: Node, list_result: list[float]) -> list[float]:
    if node.left is not None:
        _inorder(node.left, list_result)
    list_result.append(node.value)
    if node.right is not None:
        _inorder(node.right, list_result)
    return list_result

def inorder(tree: Tree) -> None:
    """
    Обход дерева в симметричном порядке.

    Args:
        node: Корень дерева.

    Returns:
        list[float]: Список значений узлов дерева в порядке обхода.
    """
    if tree.root is None:
        return []
    else:
        list_result = []
        _inorder(tree.root, list_result)
        return list_result
