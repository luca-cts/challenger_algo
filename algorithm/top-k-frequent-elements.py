from collections import Counter
from typing import List
import heapq


# tag: heap, sort
class Solution:
    """
    https://leetcode.com/problems/top-k-frequent-elements
    Counter(nums) → {1:3, 2:2, 3:1}
    heap 구성:
    Push (3, 1) → size ≤ k → ok
    Push (2, 2) → size ≤ k → ok
    Push (1, 3) → size > k → pop (1, 3) → 결과: heap = [(2, 2), (3, 1)]
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. 빈도수 카운트
        freq = Counter(nums)

        # 2. 최소 힙으로 k개 유지
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))  # 빈도 기준 min-heap
            if len(heap) > k:
                heapq.heappop(heap)

        # 3. 결과 추출 (빈도 높은 순으로 추출됨)
        return [num for count, num in heap]
