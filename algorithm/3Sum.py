from typing import List


# tag: array, two_pointer, sorting
class Solution:
    """
    https://leetcode.com/problems/3sum/description/?envType=problem-list-v2&envId=two-pointers
    세 수의 합이 0이 되는 모든 유일한 쌍을 찾는 문제, 단 중복은 허용하지 않음(인덱스 무시)
    Args:
        nums (List[int]): 숫자 배열
    Returns:
        List[List[int]]: 세 수의 합이 0이 되는 모든 유일한 세 쌍 조합
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 정렬 (O(n log n))
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # 중복된 숫자 건너뛰기
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # 중복된 값 건너뛰기
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1  # 합이 작으면 left 증가
                else:
                    right -= 1  # 합이 크면 right 감소

        return result
