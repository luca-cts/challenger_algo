from typing import List


# tag: array
class Solution:
    """
    https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i
    res = max(res, up // 2, min(pre_up, up))
    목적은: 인접한 두 increasing 구간이 있고, 둘 다 길이 ≥ k 인 경우 True를 반환해야 함
    min(pre_max_up, up):
    이전 구간과 현재 구간이 인접해 있다면, 두 구간 중 더 짧은 길이가 유효한 판단 기준
    up // 2:
    하나의 긴 increasing 구간을 반으로 나눌 수 있다면,
    예: 1, 2, 3, 4 → [1, 2], [3, 4] 처럼 → 한 구간을 두 개로 쪼갤 수 있으므로 역시 조건 만족 가능
    따라서 둘 중 큰 값을 유지:
    res = max(res, up // 2, min(pre_max_up, up))
    """

    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        up = 1  # 현재 증가 구간의 길이 (초기값: 자기 자신 포함 1)
        pre_up = 0  # 이전 증가 구간 길이 저장용
        res = 0  # 결과 최대값
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up += 1  # 증가 구간 확장
            else:
                pre_up = up  # 현재 증가 구간 종료 → 이전 값 저장
                up = 1  # 새 구간 시작
            res = max(res, up // 2, min(pre_up, up))
        return res >= k
