from typing import List
from collections import deque


# tag: bfs, matrix
class Solution:
    """
    https://leetcode.com/problems/number-of-islands/
    - bfs deque version
    - land을 만났을 때, BFS로 연결된 모든 땅을 방문 표시(`'0'`) 한다.
    - grid[r][c] == "1" 일 때, bfs(r, c)를 호출하여 섬을 모두 방문처리한다.
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            queue = deque()  # bfs
            queue.append((r, c))
            grid[r][c] = "0"  # 방문 처리

            while queue:
                row, col = queue.popleft()
                # 상하좌우 이동 방향
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        grid[nr][nc] = "0"  # 방문 처리

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":  # 새로운 섬 발견!
                    bfs(r, c)  # 섬 시작에서 연결된곳 모두 방문처리
                    islands += 1

        return islands
