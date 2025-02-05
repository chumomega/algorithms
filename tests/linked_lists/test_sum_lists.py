from LinkedListNode import LinkedListNode
from algos.linked_lists.sum_lists import sum_lists

def test_sum_lists_same_size():
    nums_list_1 = turn_list_to_linked_list([2, 4, 1])
    nums_list_2 = turn_list_to_linked_list([7, 3, 6])
    output_list = sum_lists(nums_list_1, nums_list_2)
    assert output_list.val == 9
    assert output_list.next.val == 7
    assert output_list.next.next.val == 7
    assert output_list.next.next.next == None


def test_sum_lists_diff_size():
    nums_list_1 = turn_list_to_linked_list([2, 4])
    nums_list_2 = turn_list_to_linked_list([7, 3, 6])
    output_list = sum_lists(nums_list_1, nums_list_2)
    assert output_list.val == 9
    assert output_list.next.val == 7
    assert output_list.next.next.val == 6
    assert output_list.next.next.next == None


def test_sum_lists_with_carry():
    nums_list_1 = turn_list_to_linked_list([5, 4])
    nums_list_2 = turn_list_to_linked_list([7, 9, 9])
    output_list = sum_lists(nums_list_1, nums_list_2)
    assert output_list.val == 2
    assert output_list.next.val == 4
    assert output_list.next.next.val == 0
    assert output_list.next.next.next.val == 1
    assert output_list.next.next.next.next == None


def test_sum_lists_with_zero():
    nums_list_1 = turn_list_to_linked_list([])
    nums_list_2 = turn_list_to_linked_list([7, 9, 9])
    output_list = sum_lists(nums_list_1, nums_list_2)
    assert output_list.val == 7
    assert output_list.next.val == 9
    assert output_list.next.next.val == 9
    assert output_list.next.next.next == None


def turn_list_to_linked_list(input_list: list, iter = 0) -> LinkedListNode:
    if len(input_list) == 0 or iter > len(input_list) - 1:
        return None
    head = LinkedListNode(input_list[iter])
    head.next = turn_list_to_linked_list(input_list, iter + 1)
    return head
