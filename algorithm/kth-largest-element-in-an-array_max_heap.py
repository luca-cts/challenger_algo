import heapq
from typing import List


# tag: heap, max_heap, sort
class Solution:
    """
    https://leetcode.com/problems/kth-largest-element-in-an-array/
    - max_heap 사용하고 kth heappop하기
    - sort method 사용금지
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)  # max_heap

        i = 0
        result = 0
        while i < k:  # max_heap이므로 kthlargest kth pop
            result = heapq.heappop(heap)
            i += 1

        return -result  # max_heap 위해 만든 정수값 원래대로 반환
