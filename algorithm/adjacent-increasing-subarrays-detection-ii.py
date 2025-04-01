from typing import List


# tag: binary_search, dynamic_programming
class Solution:
    """
    https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii
    prev_increase ← 이전 증가 구간의 길이
    cur_increase ← 현재 증가 구간의 길이
    배열을 순회하면서:
        nums[i] > nums[i - 1] → 증가 구간 유지: cur_increase += 1
        nums[i] <= nums[i - 1] → 증가 종료:
        현재 증가 구간을 이전 증가 구간으로 저장하고 현재 증가 구간을 1로 초기화 - 인접한 증가 구간 찾기!
    `res = max(res, cur_increase // 2, min(prev_increase, cur_increase))`
        res: 현재 최대값.
        cur_increase // 2: 현재 증가하는 서브어레이를 분할하여 형성할 수 있는 2개의 서브어레이(엄격히 증가하는 인접 서브어레이가 하나밖에 없는 경우가 생김)
        min(prev_increase, cur_increase): 이것은 이전과 현재 증가하는 하위 배열을 결합하여 더 많은 하위 배열을 형성할 수 있는 경우를 처리합니다. 우리는 두 길이 중 가장 작은 것을 취하는데, 그 이유는 두 길이 중 더 짧은 길이만큼만 하위 배열을 형성할 수 있기 때문입니다.

    """

    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev_increase, cur_increase = 0, 1
        res = 0
        for i in range(1, len(nums)):  # 이전꺼와 비교하기 때문에 idx 1부터 시작
            if nums[i] > nums[i - 1]:
                cur_increase += 1
            else:
                prev_increase, cur_increase = cur_increase, 1
            res = max(res, cur_increase // 2, min(prev_increase, cur_increase))
        return res
