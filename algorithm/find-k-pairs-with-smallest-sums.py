import heapq
from typing import List


# tag: heap
class Solution:
    """
    https://leetcode.com/problems/find-k-pairs-with-smallest-sums
    1. nums1, nums2는 각각 오름차순 정렬된 리스트이다.
    2. nums1의 요소와 nums2의 요소를 쌍지어 만들 수 있는 합 중 가장 작은 k개의 쌍을 반환하라.
    - `nums1`과 `nums2`가 정렬되어 있으므로, `nums1[0] + nums2[0]`이 가장 작음
    - 다음 작은 값은 `nums1[0] + nums2[1]` 혹은 `nums1[1] + nums2[0]`일 가능성이 높음
        - nums1[0] 값이 nums[0:k] 까지 같은 경우가 있을 수 있음
    - min-heap 을 활용하여 kth pairs를 찾는다.
    """

    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        heap = []
        res = []

        # 초기값: nums1의 0~min(k, len(nums1)) 요소 각각과 nums2[0]를 쌍지어 힙에 넣는다.
        # 이유: nums1[i] + nums2[0]은 각 행의 시작점이며, 그 중 가장 작은 합을 가진 쌍부터 탐색을 시작할 수 있기 때문이다.
        # nums1, nums2 모두 ascending order이기 때문에 가능!
        for i in range(min(len(nums1), k)):
            heapq.heappush(
                heap, (nums1[i] + nums2[0], i, 0)
            )  # (합, nums1 인덱스, nums2 인덱스)

        while heap and len(res) < k:
            sum_, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            # 다음 후보: nums1[i] + nums2[j + 1] heap에 넣어서 k개 쌍 찾을 때 까지 loop
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return res
