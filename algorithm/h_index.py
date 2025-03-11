from typing import List


# tag: sort, counting_sort
class Solution:
    """
    https://leetcode.com/problems/h-index/description/
    H-Index란 연구자가 h 편의 논문을 출판했을 때, 각 논문이 최소 h회 이상 인용된 경우의 최대 h 값을 의미한다.
    최대 n 이상의 인용은 의미가 없음 → n+1 크기의 카운트 배열을 사용.
    논문별 인용 횟수를 카운팅 후, h-index를 빠르게 찾기.
    """

    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0] * (n + 1)

        for c in citations:
            count[min(c, n)] += 1  # n 이상은 n에 포함

        h = 0
        for i in range(n, -1, -1):
            h += count[i]
            if h >= i:
                return i  # h-index 만족 조건

        return 0


s = Solution()
print(s.hIndex([3, 0, 6, 1, 5]))  # 3
print(s.hIndex([1, 3, 1]))  # 1
print(s.hIndex([0, 0, 0]))  # 0
