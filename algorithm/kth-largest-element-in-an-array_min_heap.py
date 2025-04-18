import heapq
from typing import List


# tag: heap, min_heap, sort
class Solution:
    """
    https://leetcode.com/problems/kth-largest-element-in-an-array/
    - min_heap 사용하고 kth heappop하기
    - sort method 사용금지
    - min_heap을 사용하여 k개 요소를 유지하고, 나머지 요소들과 비교하여 k번째로 큰 요소를 찾음
    - loop 요소를 줄여 시간복잡도 이득
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]  # k개수 만큼 heap 정렬 만들고
        heapq.heapify(heap)

        for num in nums[
            k:
        ]:  # 나머지 nums 요소들 loop 돌면서 heap[0] - Kth largest 찾기
            if (
                num > heap[0]
            ):  # heap[0] 보다 큰 수가 발견되면 heap[0] pop하고 큰 수 heap 정렬에 추가
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]  #  heap[0] - Kth largest
