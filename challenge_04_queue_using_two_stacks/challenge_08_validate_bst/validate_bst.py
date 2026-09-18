from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: Optional["Node"] = None, right: Optional["Node"] = None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[Node]) -> bool:
    """
    Check if the binary tree is a valid BST.
    We carry (low, high) bounds down the recursion.
    """
    def helper(node: Optional[Node], low: float, high: float) -> bool:
        if node is None:
            return True

        # Current node must be strictly inside the allowed range
        if not (low < node.val < high):
            return False

        # Left subtree: all values must be < node.val
        # Right subtree: all values must be > node.val
        return (helper(node.left, low, node.val) and
                helper(node.right, node.val, high))

    return helper(root, float("-inf"), float("inf"))


# ==================== Tests ====================
if __name__ == "__main__":
    # Valid BST
    #       5
    #      / \
    #     3   7
    #    / \
    #   2   4
    valid = Node(5,
                 left=Node(3, left=Node(2), right=Node(4)),
                 right=Node(7))
    print("Valid tree:", is_valid_bst(valid))          # True

    # Invalid BST (the classic example from the challenge)
    #       5
    #      / \
    #     1   8
    #        / \
    #       4   9          ← 4 is under 8 but 4 < 5 (violates root bound)
    invalid = Node(5,
                   left=Node(1),
                   right=Node(8, left=Node(4), right=Node(9)))
    print("Invalid tree:", is_valid_bst(invalid))      # False

    # Edge cases
    print("Empty tree:", is_valid_bst(None))           # True
    print("Single node:", is_valid_bst(Node(10)))      # True
