from typing import List


# tag: binary_search, two_pointers
class Solution:
    """
    https://leetcode.com/problems/successful-pairs-of-spells-and-potions
    물약 배열 정렬: potions 배열을 오름차순으로 정렬합니다.​
    이진 탐색 활용: 각 spell에 대해, success / spell 이상의 값을 갖는 첫 번째 potion의 위치를 이진 탐색으로 찾습니다.
    이를 통해 해당 spell과 성공적인 쌍을 형성할 수 있는 potion의 개수를 효율적으로 계산할 수 있습니다.
    """

    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        count_list = []
        potions.sort()

        for spell in spells:
            left = 0
            right = len(potions)
            while left < right:
                mid = left + (right - left) // 2  ## 반 잘라서 서치 레프트 쉬프트
                if spell * potions[mid] < success:
                    left = mid + 1
                else:
                    right = mid
            count_list.append(len(potions) - left)
        return count_list
