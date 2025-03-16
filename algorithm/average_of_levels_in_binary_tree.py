from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tag: bfs
class Solution:
    """
    https://leetcode.com/problems/average-of-levels-in-binary-tree
    - bfs - deque 생각
    - level별 모든 노드 순회
        - 노드 순회 하려면 node 숫자 파악 필요
        - avg 구하기 all val sum / lens
        - 자식노드 left, right 있으면 큐 추가
    """

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            value = 0

            for _ in range(level_size):
                node = queue.popleft()
                value += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(value / level_size)
        return result
