from bisect import bisect, bisect_left
from math import ceil


# tag: binary_search, array
class Solution:
    """
    https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays
    - 모든 정수이므로 - 값도 있음 -> include product result minus values
    - 리스트 정렬 대신 값으로 이진 탐색으로 찾는 법 사용! - count function 필요!
    - `mid`를 기준으로 `nums1[i] * nums2[j] <= mid`인 쌍의 개수를 센다
    - 그 개수가 `k` 이상이면 → `mid`는 정답 후보
    - k미만이면 오른쪽 구간 이동
    """

    def kthSmallestProduct(self, nums1, nums2, k):
        def check(x):
            total = 0
            for n1 in nums1:
                if n1 > 0:
                    total += bisect(nums2, x // n1)
                if n1 < 0:
                    total += len(nums2) - bisect_left(nums2, ceil(x / n1))
                if n1 == 0 and x >= 0:
                    total += len(nums2)

            return total

        beg, end = -(10**10) - 1, 10**10 + 1

        while beg < end:
            mid = (beg + end) // 2
            if check(mid) >= k:
                end = mid
            else:
                beg = mid + 1

        return beg
