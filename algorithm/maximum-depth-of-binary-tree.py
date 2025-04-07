class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tag: bfs, binary_tree
class Solution:
    """
    https://leetcode.com/problems/maximum-depth-of-binary-tree

    """

    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            # Use the larger one
            if left_depth > right_depth:
                return left_depth + 1
            else:
                return right_depth + 1
