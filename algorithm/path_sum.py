from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tag: dfs, binary_tree, backtracking
class Solution:
    """
    https://leetcode.com/problems/path-sum-ii/
    leaf 조건이 끝 노드를 찾아라! >> DFS
    경로 탐색 과정
    - 노드 추가: 현재 노드를 경로에 추가한 후 누적 합을 업데이트합니다.
    - 리프 노드 체크: 자식 노드가 없는 경우, 현재까지의 누적 합이 `targetSum`과 동일한지 확인합니다.
    - 재귀 호출: 왼쪽 및 오른쪽 자식 노드를 대상으로 동일한 과정을 수행합니다.
    - 백트래킹: 재귀 호출 후, 현재 노드를 경로에서 제거하여 다른 분기에서 올바른 경로를 탐색할 수 있도록 합니다
    """

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []  # 모든 유효한 경로를 저장할 리스트

        def dfs(node, path, current_sum):
            # 종료 조건: 노드가 None이면 아무것도 하지 않음
            if not node:
                return

            # 현재 노드의 값을 경로에 추가하고 누적 합 갱신
            path.append(node.val)
            current_sum += node.val

            # 리프 노드인 경우 (자식이 없는 경우)
            if not node.left and not node.right:
                # 누적 합이 targetSum과 일치하면, 현재 경로를 결과에 추가
                if current_sum == targetSum:
                    result.append(list(path))  # path의 복사본 저장
            else:
                # 왼쪽, 오른쪽 서브트리 탐색
                dfs(node.left, path, current_sum)
                dfs(node.right, path, current_sum)

            # 백트래킹: 현재 노드를 경로에서 제거하여 다른 경로에 영향 주지 않도록 함
            path.pop()

        # DFS 탐색 시작
        dfs(root, [], 0)
        return result
