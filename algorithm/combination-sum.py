from typing import List


# tag: backtracking, dfs, recursion
class Solution:
    """
    https://leetcode.com/problems/combination-sum
    - sum of combination = target => return  List[List[int]]
    - 각 엘레먼트 중복 가능
    - 조합식은 중복 안됨
    - path: 누적조합
    - current_sum: 현재까지 누적값
    - start: 현재 시작점
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(path, total, start):
            if total == target:  # 목표값 일치
                result.append(path[:])  # 조합식 정답에 추가
                return
            if total > target:  # 가지치기(탐색 끝)
                return

            for i in range(start, len(candidates)):  # idx 0부터 len(candidates) loop
                path.append(candidates[i])  # 조합에 추가
                backtrack(path, total + candidates[i], i)  # dfs recursion, i: 같은 숫자 사용 가능
                path.pop()  # 해당값이 target에 이르지 못한 조합식은 하나씩 pop후 다시 찾기

        backtrack([], 0, 0)
        return result
