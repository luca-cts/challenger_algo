from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tag: bfs, binary_tree
class Solution:
    """
    https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
    - bfs - deque
    - zigzag order traversal - 홀레벨 왼쪽 짝레벨 오른쪽 val 반환
    - 일반적인 order traversal과 같이 queue.popleft로 val 뽑고 result 추가시 레벨 홀짝에 따라 역,정순 추가
    """

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        start = 0

        while queue:
            size = len(queue)
            nodes = []
            for _ in range(size):
                node = queue.popleft()  # order traversal 같음
                nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if start % 2 != 0:  ## 홀레벨 역순 추가
                result.append(nodes[::-1])
            else:  ## 짝레벨 정순 추가
                result.append(nodes)
            start += 1
        return result
