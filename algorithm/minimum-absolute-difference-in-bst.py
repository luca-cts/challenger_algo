from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tag: tree, binary_search_tree, in_order_traversal
class Solution:
    """
    https://leetcode.com/problems/minimum-absolute-difference-in-bst/
    - BST 특징 -중위 순회(In-order Traversal) 하면 노드 값이 오름차순으로 정렬됨
    - 인접노드끼리 차이만 비교하면 최소 절대값 차이 구할 수 있음
    """

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = int("inf")

        def in_order(node):
            if not node:
                return
            in_order(node.left)

            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val

            in_order(node.right)

        in_order(root)
        return self.min_diff
