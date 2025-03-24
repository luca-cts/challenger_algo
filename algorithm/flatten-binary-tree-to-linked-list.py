from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tag: binary_tree, dfs, linked_list
class Solution:
    """
    https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
    - 이진 트리를 오른쪽으로 펼친다.
    - 왼쪽 자식은 None으로 만들고, 오른쪽 자식으로 연결한다.
    - 이전 노드 tracking을 위해 prev 변수 사용
    - 오른쪽 자식은 prev(이전 노드)로 연결한다.
    """

    def flatten(self, root: Optional[TreeNode]) -> None:
        self.prev = None  # 이전 노드 저장 (오른쪽부터 내려가며 연결)

        def dfs(node):
            if not node:
                return

            dfs(node.right)  # 오른쪽 먼저
            dfs(node.left)  # 그다음 왼쪽

            # 현재 노드의 오른쪽을 prev로 연결하고, 왼쪽은 None
            node.right = self.prev
            node.left = None
            self.prev = node  # 현재 노드를 prev로 업데이트

        dfs(root)
