from collections import deque
from typing import List


# tag: bfs, matrix
class Solution:
    """
    https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
    - 미로에서 최단 탈출경로 찾기 - entrance 위치는 출구로 취급안함, 출구는 가장자리 "." cell
    - 미로는 matrix (m * n ) - graph 탐색문제(각 위치가 노드 이동 가능한 곳 엣지)
    - 최단 거리 찾기 => bfs 사용
    - bfs deque, visited marked, search 4 direction 구현 생각
    """

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])  ## m * n matrix
        q = deque()  # bfs queue
        q.append((entrance[0], entrance[1], 0))  # (row, col, steps)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()  # 방문 마킹
        visited.add((entrance[0], entrance[1]))  # entrance init marked

        while q:
            r, c, steps = q.popleft()  # entrance 지점 시작
            for dr, dc in directions:  # 4방향 가보기
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == ".":  # 이동 조건
                    if (nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1) and (
                        nr,
                        nc,
                    ) != tuple(entrance):
                        # 가장자리에 있는지 확인 and entrance는 출구 아님 조건 검사
                        return steps + 1  # 이동 횟수 증가
                    maze[nr][nc] = "+"  # 방문 마킹
                    q.append((nr, nc, steps + 1))  # 다음칸 bfs queue 넣기

        return -1  # 출구 없을 최후 조건
