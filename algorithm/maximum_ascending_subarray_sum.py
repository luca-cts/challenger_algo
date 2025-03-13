from typing import List


# tag: array, subarray
class Solution:
    """
    https://leetcode.com/problems/maximum-ascending-subarray-sum/
    오름차순으로 증가하는 구간을 찾으면서 합을 계산.
    값이 감소하면 새로운 부분 배열 시작.
    최대 부분 합을 갱신하며 진행.
    """

    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0
        temp = nums[0]
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:  # 오름차순 계속 합
                temp += nums[i + 1]
            else:  # 새 배열 시작
                result = max(result, temp)
                temp = nums[i + 1]  # 새 배열의 새 값 시작

        return max(result, temp)
