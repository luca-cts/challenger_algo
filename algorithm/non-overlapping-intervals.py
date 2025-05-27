from typing import List


# tag: greedy, dp, sorting
class Solution:
    """
    https://leetcode.com/problems/non-overlapping-intervals
    - 주어진 구간들 중 겹치는 구간을 제거하여, 남은 구간들이 서로 겹치지 않도록 하는 최소 개수
    - end가 작을 수록 안겹칠 확률이 높음
    - end 기준으로 ordering
    - this end > next start -> 겹침 -> 제거
    - 그리디 알고리즘
    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  # 끝나는 시간 기준 정렬
        remove = 0
        prev_end = float("-inf")

        for start, end in intervals:
            if start < prev_end:  # 겹침
                remove += 1
            else:
                prev_end = end  # 갱신

        return remove
