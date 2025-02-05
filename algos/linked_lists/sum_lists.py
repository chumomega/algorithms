from LinkedListNode import LinkedListNode

def sum_lists(l1: LinkedListNode, l2: LinkedListNode) -> LinkedListNode:
    return sum_lists_with_carry(l1, l2, 0)


def sum_lists_with_carry(l1: LinkedListNode, l2: LinkedListNode, carry: int) -> LinkedListNode:
    if l1 is None and l2 is None and carry == 0:
        return None
    sum = carry
    new_carry = 0

    if l1 is not None:
        sum += l1.val
    if l2 is not None:
        sum += l2.val
    
    # only 1 integer per linked list node
    if sum > 9:
        sum = sum % 10
        new_carry = 1
    
    return_node = LinkedListNode(sum)
    next_node = sum_lists_with_carry(
        l1.next if l1 is not None else None, 
        l2.next if l2 is not None else None, 
        new_carry
    )
    return_node.next = next_node
    return return_node
    
    