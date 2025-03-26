import heapq


# tag: heap, matrix, sorting
class Solution:
    """
    https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix
    - 지속적으로 extract value to k times
    - find-k-pairs-with-smallest-sums.py 유사 참고
    - 가장 최근 row 값이 작긴하지만 row 안에서 ascending이 되기 때문에 다음 row에서 작은값이 충분히 있을 수 있음
    -> value 비교를 해야함 -> kth times 동안 min-heap heappush 진행(다음 col로)
    """

    def kthSmallest(self, matrix, k):
        n = len(matrix)
        heap = []

        # Step 1: Start by pushing the first element of each row (just row 0)
        for i in range(min(n, k)):
            heapq.heappush(heap, (matrix[i][0], i, 0))  # (value, row, col)

        # Step 2: Pop the smallest element k times
        count = 0
        while heap:
            val, r, c = heapq.heappop(heap)
            count += 1
            if count == k:
                return val
            # Step 3: Push the next element in the same row
            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
