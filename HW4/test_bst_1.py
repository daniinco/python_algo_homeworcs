from bst_1 import Tree, preorder, inorder, postorder

def test_orders():
    tree = Tree()
    tree.add(2)
    tree.add(1)
    tree.add(4)
    tree.add(3)
    tree.add(-1)
    tree.add(0)
    tree.add(6)
    tree.add(5)
    tree.add(7)
    assert preorder(tree) == [2, 1, -1, 0, 4, 3, 6, 5, 7]
    assert inorder(tree) == [-1, 0, 1, 2, 3, 4, 5, 6, 7]
    assert postorder(tree) == [0, -1, 1, 3, 5, 7, 6, 4, 2]