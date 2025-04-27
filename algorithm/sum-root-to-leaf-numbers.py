from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tag: tree, dfs
class Solution:
    """
    https://leetcode.com/problems/sum-root-to-leaf-numbers/
    - 루트 → 리프까지 "경로를 따라가는" 문제
    - 경로를 따라가는 문제는 DFS로 해결하는 것이 일반적
    - 자리수 누적
    - leaf 노드 = left, right가 모두 None인 노드 => return current_sum
    """

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum = current_sum * 10 + node.val

            if not node.left and not node.right:
                return current_sum

            # 왼쪽과 오른쪽 서브트리 결과를 합친다
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)
