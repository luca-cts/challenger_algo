from collections import defaultdict
from typing import List


# tag: graph, dfs
class Solution:
    """
    https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero
    - 도시, 도로 -> 도로는 도시 -1
    - 양방향 탐색 필요 => dfs(방향정보 args 필요할듯)
    - 중복 탐색 방지를 위한 방문 도시 기록
    - 이웃 도시 방문하는데 방문하지 않는 경우 연결 방향 확인
        - from == cur_node -> 0으로 안감 -> 방향 체인지
        - to == cur_node -> 0으로 감 -> 그대로
    - 이웃 도시 -> 현재도시 재귀 dfs
    - 시작은 0부터 시작
    """

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in connections:
            # 양방향 연결 만듬
            graph[u].append((v, 1))  # u → v: 원래 방향
            graph[v].append((u, 0))  # v → u: 역방향 (도로 방향 X)

        visited = set()

        def dfs(node):
            visited.add(node)  # 현재 도시 방문
            changes = 0

            for neighbor, direction in graph[node]:
                if neighbor not in visited:  # 방문하지 않는 도시만
                    changes += direction  # node -> neighbor 상태 이때 direction == 1 이면 정방향인데 방문을 안했으면 역방향으로 바꿔야됨
                    changes += dfs(neighbor)  # dfs 재귀 탐색하면서 changes 누적

            return changes

        return dfs(0)
