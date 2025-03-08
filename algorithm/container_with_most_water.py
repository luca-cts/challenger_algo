from typing import List


# tag: two-pointer, array, greedy
class Solution:
    """
    https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75
    Args: height (List[int]): 기둥의 높이 리스트
    return: int: 가장 많은 물을 담을 수 있는 최대 넓이
    """

    def maxArea(self, height: List[int]) -> int:
        max_area = 0  # save max value init 0
        left = 0  # two-pointer start left
        right = len(height) - 1  # two-pointer start right

        while left < right:  # two-pointer do not cross
            width = right - left
            area = min(height[left], height[right]) * width  # 기둥의 최소높이 기준
            max_area = max(max_area, area)

            if height[left] < height[right]:  # 안으로 들어가기, 기둥 높이 낮은거 이동
                left += 1
            else:
                right -= 1

        return max_area
