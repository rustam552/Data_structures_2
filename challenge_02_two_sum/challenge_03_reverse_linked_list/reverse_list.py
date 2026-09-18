from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, val: int = 0, next: Optional["Node"] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        vals = []
        curr = self
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        return " → ".join(vals) + " → None"


def reverse_list(head: Optional[Node]) -> Optional[Node]:
    """Iterative version – O(n) time, O(1) space"""
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def reverse_list_recursive(head: Optional[Node]) -> Optional[Node]:
    """Recursive version – O(n) time, O(n) space (call stack)"""
    if head is None or head.next is None:
        return head

    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


def build_list(values: list[int]) -> Optional[Node]:
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for v in values[1:]:
        curr.next = Node(v)
        curr = curr.next
    return head


# ===== Tests =====
if __name__ == "__main__":
    print("=== Iterative ===")
    head1 = build_list([1, 2, 3])
    print("Original:", head1)
    print("Reversed:", reverse_list(head1))
    print()

    print("=== Recursive ===")
    head2 = build_list([1, 2, 3, 4, 5])
    print("Original:", head2)
    print("Reversed:", reverse_list_recursive(head2))
