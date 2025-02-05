from typing import Optional
class LinkedListNode:
    def __init__(self, val, next: Optional["LinkedListNode"] = None):
        self.val = val
        self.next = next
