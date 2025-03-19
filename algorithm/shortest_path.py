from collections import deque


# tag: bfs, greedy
def solution(maps):
    """
    https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3
    - BFS 사용: 너비 우선 탐색을 사용하여 가장 가까운 노드부터 탐색합니다.
    - 방문 배열: `visited` 배열을 사용하여 각 위치까지의 최단 거리를 기록합니다.
    - 방향 이동: 상하좌우 네 방향으로 이동할 수 있습니다.
    - 유효성 검사: 이동할 위치가 맵 범위 내에 있고, 벽이 아니며, 아직 방문하지 않았는지 확인합니다.
      최종적으로, 만약 목적지에 도달할 수 없으면 `visited[n-1][m-1]`의 값은 -1이 됩니다. 도달할 수 있다면 시작점부터 목적지까지의 최단 거리를 반환합니다.
    """
    n = len(maps)  # 행의 개수
    m = len(maps[0])  # 열의 개수

    # 이동 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 방문 여부와 거리를 기록할 배열 초기화
    visited = [[-1 for _ in range(m)] for _ in range(n)]

    # BFS 시작
    queue = deque([(0, 0)])  # (1,1)을 0-indexed로 변환하면 (0,0)
    visited[0][0] = 1  # 시작 위치의 거리는 1

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵 범위 내에 있고, 벽이 아니며, 아직 방문하지 않은 경우
            if (
                0 <= nx < n
                and 0 <= ny < m
                and maps[nx][ny] == 1
                and visited[nx][ny] == -1
            ):
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    # 상대 진영 위치의 최단 거리 반환
    return visited[n - 1][m - 1]


# 예시
maps1 = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
]
print(solution(maps1))  # 11

maps2 = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
]
print(solution(maps2))  # -1
