from typing import List


# tag: greedy, sorting, interval_scheduling
class Solution:
    """
    https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
    - 구간 `[a1, a2]`, `[b1, b2]`일 때
    - `max(a1, b1) ≤ min(a2, b2)`
    - greedy
    - 겹치는 구간을 count +=1, 다음 겹치는 구간 count +=1
    - 끝나는 시점 정렬, 겹치는 범위 최소화
    """

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])  # 끝나는 지점 기준 정렬
        count = 0
        prev_end = float("-inf")

        for s, e in points:
            if s > prev_end:  # 겹치지 않으면 새로운 화살 필요
                count += 1
                prev_end = e  # 이 화살로 끝나는 위치까지만 커버됨

        return count
