import pytest
from merge_lists import merge_lists, merge_lists_with_fictive, ConnectedList, ConnectedListWithFictive

def test_empty_lists():
    list1 = ConnectedList()
    list2 = ConnectedList()
    merged_list_head = merge_lists(list1, list2)
    assert merged_list_head is None

    list1 = ConnectedList()
    list2 = ConnectedList()
    merged_list_head = merge_lists_with_fictive(list1, list2)
    assert merged_list_head.value == float("inf")

def test_merge_lists_without_fictive_nodes():
    test_values = [
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([], [4, 5, 6], [4, 5, 6]),
        ([1, 4, 5, 6], [2, 3, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([-2], [-2, 1, 3], [-2, -2, 1, 3]),
        ([1, 2, 3, 7], [3, 4, 5], [1, 2, 3, 3, 4, 5, 7])
    ]
    for test in test_values:
        list1 = ConnectedList(test[0])
        list2 = ConnectedList(test[1])
        merged_list_head = merge_lists(list1, list2)
        assert list(i for i in merged_list_head) == test[2]

        list1 = ConnectedListWithFictive(test[0])
        list2 = ConnectedListWithFictive(test[1])
        merged_list_head = merge_lists_with_fictive(list1, list2)
        assert list(i for i in merged_list_head) == test[2]