from collections import deque


# tag: bfs, matrix
def orangesRotting(grid):
    """
    https://leetcode.com/problems/rotting-oranges/
    - rotten orange를 먼저 순회로 찾고 deque에 위치 좌표 넣기(bfs)
    - rotten orange 위치에서 4 direction 재귀 돌리기? >> dfs?( 한 방향마다 갈 수 있는 곳 까지 가는 개념)
    - [택] rotten 기준으로 주변의 오렌지 건드려야 >> bfs(시작 기준으로 모든방향 다찾고 그 다음 위치에서 모든 방향 다찾는 개념)
        - fresh면 2로 바꾸고 큐에 넣기!
    - 한 레벨당 시간 증가 개념으로 - while queue 하면서 마지막에 시간 += 1
    - 최후의 오렌지가 남아 있는지 또 다시 grid loop??? >> fresh orange 개수 먼저 파악 해놓고 카운트 세면 시간복잡도 줄일 수 있음!
    """
    m, n = len(grid), len(grid[0])  # x, y size
    queue = deque()  # bfs deque
    fresh = 0  # 종료조건을 위한

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # append deque rotten location and time
            elif grid[r][c] == 1:  # fresh count 파악
                fresh += 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    minutes = 0  # 총 걸리는 시간

    while queue:
        x, y, time = queue.popleft()  # rotten orange location, time
        minutes = max(minutes, time)  # 레벨별 맥스값
        for dx, dy in directions:  # 4 방향 가보기
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:  # fresh 만남
                grid[nx][ny] = 2  # 썩고
                fresh -= 1  # 총 프레쉬 감소
                queue.append(
                    (nx, ny, time + 1)
                )  # append deque new rotten location and time

    return (
        minutes if fresh == 0 else -1
    )  # fresh가 없으면 총 걸리는 시간, fresh가 남아 있으면 실패 -1 리턴
