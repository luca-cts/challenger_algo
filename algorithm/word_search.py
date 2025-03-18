from typing import List


# tag: dfs, array, backtracking, matrix
class Solution:
    """
    https://leetcode.com/problems/word-search/description/
    dfs 재귀 호출를 통해 해를 찾는 문제
    재귀함수 종료조건
    - `k == len(word)`: 모든 문자를 성공적으로 찾은 경우 `True`를 반환합니다.
    - 인덱스가 보드의 범위를 벗어나거나, 현재 칸의 문자가 단어의 k번째 문자와 일치하지 않으면 `False`를 반환합니다.
    방문 처리 및 재귀 탐색
    - 현재 칸의 문자를 임시 변수 `tmp`에 저장하고, 방문 표시로 `"#"`로 변경합니다.
    - 상하좌우 네 방향으로 다음 문자(`word[k+1]`)를 찾기 위해 재귀 호출합니다.
    - 재귀 탐색 후, 원래 값으로 복원합니다.
    보드의 모든 위치를 순회하며, 해당 칸에서 DFS를 시작합니다.
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])  # 행과 열의 크기를 미리 구함

        # DFS를 통한 백트래킹 함수 정의
        def dfs(i, j, k):
            # k가 단어의 길이와 같으면, 모든 문자를 찾은 것임
            if k == len(word):
                return True
            # 좌표가 범위를 벗어나거나 현재 칸의 문자가 단어의 k번째 문자와 다르면 False
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
                return False

            # 현재 위치를 방문 처리하기 위해 임시로 값을 저장 후, 특수 문자로 변경 (중복 방문 방지)
            tmp = board[i][j]
            board[i][j] = "#"

            # 상하좌우 방향으로 다음 문자(word[k+1])를 찾기 위해 재귀 호출
            found = (
                dfs(i + 1, j, k + 1)
                or dfs(i - 1, j, k + 1)
                or dfs(i, j + 1, k + 1)
                or dfs(i, j - 1, k + 1)
            )

            # 재귀 탐색 후, 원래 값으로 복원 (백트래킹)
            board[i][j] = tmp

            return found

        # 보드의 모든 위치에서 DFS 탐색 시작
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
