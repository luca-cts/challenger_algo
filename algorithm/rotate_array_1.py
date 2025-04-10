from typing import List


# tag: array, two_pointers
class Solution:
    """
    https://leetcode.com/problems/rotate-array
    k는 배열의 길이보다 클 수 있으므로, k를 len(nums)로 나눈 나머지를 사용하여 실제 회전할 만큼만 계산합니다.
    슬라이스를 사용하여 배열을 회전합니다.
    nums[:] => in-place로 nums를 수정합니다.(mutable)
    """

    def rotate(self, nums: List[int], k: int) -> List[int]:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums
