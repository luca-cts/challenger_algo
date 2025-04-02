from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tag: bfs, binary_tree
class Solution:
    """
    https://leetcode.com/problems/binary-tree-right-side-view
    - BFS를 사용하여 각 레벨의 마지막 노드를 추출합니다.
    - deque를 사용하여 레벨 순회합니다.
    - 각 레벨을 순회하면서 마지막 노드의 값을 결과 리스트에 추가합니다.
    """

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:  # 트리가 비어 있으면 빈 리스트 반환
            return []
        res = []
        queue = deque([root])  # bfs queue init
        while queue:
            size = len(queue)  # 현재 레벨의 노드 수
            for i in range(size):
                node = queue.popleft()
                if i == size - 1:
                    res.append(node.val)  # 현재 레벨의 마지막 노드 값(오른쪽) 저장
                if node.left:  # 다음레벨 자식 노드를 큐에 추가
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res
