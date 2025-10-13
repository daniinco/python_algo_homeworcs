from bst_3 import Tree, is_balansed, Node

def test_bst_is_balansed():
    tree = Tree()
    tree.add(4)
    assert is_balansed(tree) == True
    tree.add(2)
    assert is_balansed(tree) == True
    tree.add(1)
    assert is_balansed(tree) == False
    tree.add(3)
    assert is_balansed(tree) == False
    tree.add(6)
    assert is_balansed(tree) == True
    tree.add(5)
    assert is_balansed(tree) == True
    tree.add(7)
    assert is_balansed(tree) == True
    tree.add(8)
    tree.add(3.5)
    assert is_balansed(tree) == True
    tree.add(3.75)
    assert is_balansed(tree) == False