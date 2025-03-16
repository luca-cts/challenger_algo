from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tag: bfs
class Solution:
    """
    https://leetcode.com/problems/binary-tree-level-order-traversal/
    - bfs - deque 생각
    - level list group, order left to right
    - level별 모든 노드 순회
        - 노드 순회 하려면 level에 node 개수 파악이 우선
        - lvl에 있는 node 개수 만큼 popleft 진행
        - 자식노드 left, right 있으면 큐 추가
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:  # 큐가 빌 때까지 반복
            level_size = len(queue)  # 현재 레벨의 노드 개수
            level_nodes = []  # 현재 레벨의 값 저장

            for _ in range(level_size):
                node = queue.popleft()  # 큐에서 노드 꺼내기
                level_nodes.append(node.val)  # 값 저장

                if node.left:
                    queue.append(node.left)  # 왼쪽 자식 추가
                if node.right:
                    queue.append(node.right)  # 오른쪽 자식 추가

            result.append(level_nodes)  # 해당 레벨의 값 저장

        return result
