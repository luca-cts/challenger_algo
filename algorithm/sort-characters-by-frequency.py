from collections import Counter
import heapq


# tag: heap, sorting
class Solution:
    """
    https://leetcode.com/problems/sort-characters-by-frequency
    각 문자의 빈도 수 카운트
    빈도 수를 기준으로 우선순위 큐(Heap) 에 저장
    빈도 수가 높은 문자부터 꺼내서 결과 문자열 생성
    """

    def frequencySort(self, s: str) -> str:
        # 1. 문자 빈도 카운트
        counter = Counter(s)

        # 2. 힙에 (-freq, char) 형태로 저장 (최대 힙처럼 동작)
        heap = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(heap)

        # 3. 힙에서 꺼내서 결과 문자열 구성
        result = []
        while heap:
            freq, char = heapq.heappop(heap)
            result.append(char * (-freq))  # freq는 음수 → 양수로 곱함

        return "".join(result)
