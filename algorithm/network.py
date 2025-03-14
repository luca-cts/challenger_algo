# tag: stack, dfs, recursive
def solution(n, computers):
    """
    https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3
    대각선(`computers[i][i]`)은 항상 1이며, 만약 `computers[i][j]`가 1이면 컴퓨터 i와 j가 직접 연결됨!
    연결된 컴퓨터를 구할때 방문 처리 리스트를 이용해 중복 방문 방지
    - **DFS(깊이 우선 탐색):**
        - `dfs(i)` 함수는 컴퓨터 i와 직접 또는 간접적으로 연결된 모든 컴퓨터를 탐색합니다.
        - 만약 `computers[i][j]`가 1이고 아직 방문하지 않았다면, 컴퓨터 j를 방문한 후 `dfs(j)`를 재귀적으로 호출하여 연결된 모든 컴퓨터를 처리합니다.
    - **네트워크(연결 요소) 계산:**
        - 모든 컴퓨터를 순회하면서 아직 방문하지 않은 컴퓨터 i가 있다면, 이는 새로운 네트워크의 시작점입니다.
        - 해당 컴퓨터를 시작으로 DFS를 진행하여 그 네트워크에 속한 모든 컴퓨터를 방문 처리한 후, 네트워크 개수(`count`)를 증가시킵니다.
        - 모든 컴퓨터에 대해 이 과정을 반복하면 최종적으로 전체 네트워크의 개수를 얻을 수 있습니다
    """
    visited = [False] * n  # 각 컴퓨터가 방문되었는지 체크하기 위한 리스트

    def dfs(i):
        # 컴퓨터 i와 연결된 모든 컴퓨터를 탐색하는 재귀 함수
        for j in range(n):
            # i와 j가 연결되어 있고 아직 방문하지 않은 경우
            if computers[i][j] == 1 and not visited[j]:
                visited[j] = True
                dfs(j)

    count = 0  # 네트워크(연결 요소)의 개수를 저장할 변수
    for i in range(n):
        if not visited[i]:
            # 새로운 네트워크를 발견하면 개수를 증가시키고 DFS로 연결된 컴퓨터들을 방문 처리
            count += 1
            visited[i] = True
            dfs(i)

    return count
