from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tag: binary_tree, dfs
class Solution:
    """
    https://leetcode.com/problems/validate-binary-search-tree/
    - 루트 노드의 값은 무한한 범위에서 시작
    - 왼쪽 서브트리는 항상 `val < root.val`
    - 오른쪽 서브트리는 항상 `val > root.val`
    - 이 범위를 재귀적으로 내려가면서 확인
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True

            # 현재 노드가 허용된 범위를 벗어나면 False
            if not (low < node.val < high):
                return False

            # 왼쪽 서브트리는 upper bound가 node.val
            # 오른쪽 서브트리는 lower bound가 node.val
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float("-inf"), float("inf"))
