from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tag: bfs, binary_tree
class Solution:
    """
    https://leetcode.com/problems/maximum-width-of-binary-tree/
    - 루트 노드를 0번 인덱스로 설정하고 큐에 삽입 > `deque([(root, 0)])`
    - node.left - idx 2*n 으로
    - node.right - idx 2*n +1 (level 1 right idx 1 )
    """

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # 루트가 없으면 너비는 0

        queue = deque([(root, 0)])  # BFS를 위한 큐 (노드, 인덱스)
        max_width = 0  # 최대 너비 저장

        while queue:
            lev_len = len(queue)  # 현재 레벨의 노드 개수
            _, start = queue[0]  # 현재 레벨의 첫 번째 노드 인덱스 (왼쪽 끝)

            for i in range(lev_len):
                node, idx = queue.popleft()  # 현재 노드 및 인덱스 가져오기

                # 왼쪽 자식이 있으면 인덱스: 2 * idx
                if node.left:
                    queue.append((node.left, 2 * idx))

                # 오른쪽 자식이 있으면 인덱스: 2 * idx + 1
                if node.right:
                    queue.append((node.right, 2 * idx + 1))

            # 현재 레벨의 너비 계산 (마지막 노드 인덱스 - 첫 번째 노드 인덱스 + 1)
            max_width = max(max_width, idx - start + 1)

        return max_width  # 최대 너비 반환
