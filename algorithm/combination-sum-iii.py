from typing import List


# tag: backtracking, dfs, recursion
class Solution:
    """
    https://leetcode.com/problems/combination-sum-iii
    제약조건: k개 숫자 유니크(중복방지), target: n(sum of combination)이면 정답 저장
    """

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int], total: int):
            if len(path) == k:
                if total == n:
                    result.append(path[:])
                return

            for i in range(start, 10):
                if total + i > n:
                    break

                path.append(i)
                backtrack(i + 1, path, total + i)
                path.pop()

        backtrack(1, [], 0)
        return result
