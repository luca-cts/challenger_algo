from typing import List


# tag: dfs, matrix
class Solution:
    """
    https://leetcode.com/problems/number-of-islands/
    - 방문 dfs
    - land을 만났을 때, DFS로 연결된 모든 땅을 방문 표시(`'0'`) 한다.
    - 이렇게 하면 한 번의 DFS로 하나의 섬 전체를 탐색하게 됨.
    - 방문한 땅은 '0'으로 바꾸거나 visited로 관리하여 다시 세지 않도록 함.
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            grid[r][c] = "0"  # 방문 처리 (물로 바꿔버림)
            dfs(r + 1, c)  # 아래
            dfs(r - 1, c)  # 위
            dfs(r, c + 1)  # 오른쪽
            dfs(r, c - 1)  # 왼쪽

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands
