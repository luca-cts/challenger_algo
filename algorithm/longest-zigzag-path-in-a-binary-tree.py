from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tag: binary_tree, dfs
class Solution:
    """
    https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
    - 노드 레벨마다 방향 전환
    - 전역변수로 경로 길이 지정
    - 각 노드마다 왼쪽, 오른쪽인 2개의 경로 초이스가 있음
        - 왼쪽인경우 > 오른쪽 > 왼쪽 > .. 경로 길이가 늘어남 - max 함수로 update
                - 왼쪽인경우 경로 1로 초기화해서 max 함수로 무시
        - 오른쪽인경우 > 왼쪽 > 오른쪽 > .. 경로 길이가 늘어남 - max 함수로 update
                - 오른쪽인 경우 경로 1로 초기화해서 max 함수로 무시
    - 최대 길이 경로 구하기
    """

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0

        def dfs(node, direction, length):
            if not node:
                return

            self.max_len = max(self.max_len, length)

            if direction == "left":
                # 왼쪽 → 오른쪽
                dfs(node.right, "right", length + 1)
                # 왼쪽 → 왼쪽 (restart) 재시작해서 길이 1로 max함수로 무시됨
                dfs(node.left, "left", 1)
            else:
                # 오른쪽 → 왼쪽
                dfs(node.left, "left", length + 1)
                # 오른쪽 → 오른쪽 (restart) 재시작해서 길이 1로 max함수로 무시됨
                dfs(node.right, "right", 1)

        # 양쪽 방향 모두 root부터 시작
        dfs(root.left, "left", 1)
        dfs(root.right, "right", 1)

        return self.max_len
