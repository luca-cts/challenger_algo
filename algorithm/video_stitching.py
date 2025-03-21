from typing import List


# tag: greedy, dynamic_programming, array
class Solution:
    """
    https://leetcode.com/problems/video-stitching/
    - 항상 현재 위치에서 가장 멀리 도달할 수 있는 클립을 선택 (Greedy).
    - 핵심:::: 클립들을 `start` 기준으로 오름차순 정렬!!
    - 현재 커버 가능한 구간을 유지하면서, 최대한 커버를 확장하는 클립들을 선택을 위한 loop
    """

    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # 1. 시작시간 기준 정렬
        clips.sort(key=lambda x: (x[0], -x[1]))

        count = 0  # 선택한 클립 수
        cur_end = 0  # 현재 커버되는 끝 구간
        i = 0
        n = len(clips)

        while cur_end < T:
            farthest = cur_end  # 이번 단계에서 가장 멀리 갈 수 있는 지점

            # 2. 현재 구간 내에서 갈 수 있는 가장 먼 end를 찾는다
            while i < n and clips[i][0] <= cur_end:
                farthest = max(farthest, clips[i][1])
                i += 1

            # 더 이상 확장 못하면 실패
            if farthest == cur_end:
                return -1

            # 확장 성공 → 클립 선택
            count += 1
            cur_end = farthest

        return count
