# tag: dynamic_programming, tiling
class Solution:
    """
    https://leetcode.com/problems/domino-and-tromino-tiling/
    - 점화식
    - `dp[n] = 2 * dp[n-1] + dp[n-3]`
    -
    | 항목 | 설명 |
    |---|---|
    | `dp[n-1]` | 마지막에 세로 도미노 1개 붙인 경우 |
    | `dp[n-2]` | 마지막에 가로 도미노 2개 붙인 경우 |
    | `dp[n-3]` | 트로미노를 하나 붙이는 경우 (회전 포함 2가지, 대칭 포함 시 누적되는 것) |
    | `2 * dp[n-1] + dp[n-3]` | 최적화된 점화식 (상태 누적값을 압축) |
    """

    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[n]
