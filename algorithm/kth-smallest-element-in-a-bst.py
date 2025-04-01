from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tag: bst, inorder_traversal, bfs
class Solution:
    """
    https://leetcode.com/problems/kth-smallest-element-in-a-bst
    - 중위 순회(Inorder Traversal) 이용:
        - 중위 순회는 왼쪽 자식 → 현재 노드 → 오른쪽 자식 순으로 노드를 방문합니다.
        - 이 순서로 방문하면 BST의 값들이 오름차순으로 정렬되므로, k번째 방문한 노드가 k번째 작은 원소가 됩니다.
    - 구현 방법:
        - 인스턴스 변수 사용:
        `self.k`와 `self.ans`를 사용하여 재귀 호출 사이에서도 k의 값을 유지하고, 정답을 저장합니다.
        - 재귀 함수 `inorder`:
            - 왼쪽 서브트리를 먼저 순회합니다.
            - 현재 노드를 방문할 때마다 `self.k`를 감소시키고, 0이 되면 해당 노드의 값을 `self.ans`에 저장합니다.
            - 오른쪽 서브트리 순회.
        - 조기 종료:
        현재 코드에서는 단순화를 위해 조기 종료를 위한 추가 조건은 없지만, `self.k`가 0이 되면 이후의 호출에서 더 이상의 처리를 하지 않아도 되므로 개선할 수도 있습니다.
    """

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # k의 값을 직접 감소시키며 순회하기 위해 인스턴스 변수를 사용
        self.k = k
        self.ans = None

        def inorder(node):
            if not node:
                return
            # 왼쪽 서브트리 먼저 방문 (BST에서 왼쪽은 작은 값)
            inorder(node.left)
            # 현재 노드 방문: k 값을 1 감소시키고, k가 0이면 kth 작은 원소를 찾은 것
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return
            # 오른쪽 서브트리 방문
            inorder(node.right)

        inorder(root)
        return self.ans
