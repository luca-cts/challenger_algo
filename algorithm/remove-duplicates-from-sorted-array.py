from typing import List


# tag: two_pointers
class Solution:
    """
    https://leetcode.com/problems/remove-duplicates-from-sorted-array
    - 정렬된 배열에서 중복된 숫자를 제거하고 고유한 숫자의 개수를 반환
    - 중복을 제거해서 각 원소가 최대 1번씩만 등장하게 만들고, 그 결과를 배열 앞쪽에 채워야 함 (in-place)
    - two pointers를 사용!!
        - slow: 고유한 값이 채워질 위치
        - fast: 배열을 따라가면서 중복인지 아닌지 확인
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        slow = 1  # 고유값을 덮어 쓸 위치
        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1

        return slow
