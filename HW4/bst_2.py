from bst_1 import Tree, Node


def _is_bst(node: Node) -> bool:
    if node.left is not None:
        if not _is_bst(node.left):
            return False
        if node.left.max().value >= node.value:
            return False
    if node.right is not None:
        if not _is_bst(node.right):
            return False
        if node.right.min().value <= node.value:
            return False
    return True

def is_bst(tree: Tree) -> bool:
    """
    Проверка дерева на то, является ли оно бинарным деревом поиска.

    Args:
        tree: Дерево.

    Returns:
        bool: True, если дерево является бинарным деревом поиска, иначе False.
    """
    if tree.root is None:
        return True
    return _is_bst(tree.root)