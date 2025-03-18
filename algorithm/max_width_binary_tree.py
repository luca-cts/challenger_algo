from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tag: binary_tree, bfs, deque
class Solution:
    """
    https://leetcode.com/problems/maximum-width-of-binary-tree/
    최대 길이 찾기 - 루트부터 가까운 노드부터 차근차근, 레이어 서치 끝내고 다음 레이어로 넘어가는 개념
    bfs deque 사용
    """

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:  # 빈 트리면 0 반환
            return 0

        queue = deque([(root, 0)])  # 노드 및 인덱스를 저장할 deque 생성
        max_width = 0  # 최대 너비 결과값

        while queue:  # queue가 빌 때까지 반복
            level_length = len(queue)
            _, level_start = queue[0]  # [(root, 0)] -> 0

            for i in range(level_length):
                node, index = queue.popleft()

                if node.left:  # 왼쪽 노드가 있으면 인덱스 2n 저장
                    queue.append((node.left, 2 * index))

                if node.right:  # 오른쪽 노드가 있으면 인덱스 2n + 1 저장
                    queue.append((node.right, 2 * index + 1))

            max_width = max(
                max_width, index - level_start + 1
            )  # 최대 너비 갱신 (인덱스 차이 + 1)

        return max_width
