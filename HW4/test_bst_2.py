from bst_2 import Tree, is_bst, Node

def test_bst_is_bst():
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
    assert is_bst(tree) == True

def test_bst_is_not_bst():
    tree = Tree()
    tree.add(10)
    tree.add(4)
    tree.add(2)
    tree.add(1)
    tree.add(3)
    tree.add(6)
    tree.add(5)
    tree.add(7)

    node = tree.root.get_by_value(2)
    node.value = 4
    assert is_bst(tree) == False
    node.value = 2
    
    node = tree.root.get_by_value(6)
    node.value = 4
    assert is_bst(tree) == False
    node.value = 6

    node = tree.root.get_by_value(3)
    node.value = 4
    assert is_bst(tree) == False
    node.value = 3

    node = tree.root.get_by_value(5)
    node.value = 4
    assert is_bst(tree) == False
    node.value = 5

    node = tree.root.get_by_value(1)
    node.value = 2
    assert is_bst(tree) == False
    node.value = 1