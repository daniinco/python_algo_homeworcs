from bst_1 import Tree, Node

def _is_balansed(node: Node) -> tuple[bool, int]:
    if node.left is not None:
        left_balansed, left_height = _is_balansed(node.left)
        if not left_balansed:
            return False, 0
    else:
        left_height = 0
    if node.right is not None:
        right_balansed, right_height = _is_balansed(node.right)
        if not right_balansed:
            return False, 0
    else:
        right_height = 0
    if abs(left_height - right_height) > 1:
        return False, 0
    return True, max(left_height, right_height) + 1

def is_balansed(tree: Tree) -> bool:
    """
    Проверка дерева на то, является ли оно сбалансированным.

    Args:
        tree: Дерево.

    Returns:
        bool: True, если дерево является сбалансированным, иначе False.
    """
    if tree.root is None:
        return True
    return _is_balansed(tree.root)[0]
