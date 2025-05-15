from typing import List


# dynamic_programming
class Solution:
    """
    https://leetcode.com/problems/house-robber
    - dp 문제
    - dp[0], dp[1] 시작해서 step 2로 loop sum하는데
    - dp[2]부터 시작해서 건너뛰거나 더하거나 이 2개 비교해서 max값을 dp[i]에 저장
    - step 2로 loop sum 할 수 있고 2개의 2 step loop를 비교 가능
    - 집이 한채면 그 집을 털고 끝
    - 집이 두채면 더 큰 집을 털고 끝
    - 집이 세채면 첫번째 집을 털고 두번째 집은 털지 않고 세번째 집을 털거나 두 번째 집만 털거나
    """

    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]
