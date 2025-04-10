from typing import List


# tag: array, two_pointers
class Solution:
    """
    https://leetcode.com/problems/rotate-array
    배열을 k만큼 회전하는 문제입니다. 버전2
    배열을 뒤집는 아이디어를 활용 → 정방향 회전을 역방향 뒤집기로 구현
    """

    def rotate(self, nums: List[int], k: int) -> List[int]:
        k %= len(nums)

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # 전체 뒤집기
        reverse(0, len(nums) - 1)
        # 앞쪽 k개 뒤집기
        reverse(0, k - 1)
        # 나머지 뒤집기
        reverse(k, len(nums) - 1)
        return nums


print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3))
