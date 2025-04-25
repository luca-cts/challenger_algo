from typing import List


# tag: stack, monotonic_stack
class Solution:
    """
    https://leetcode.com/problems/daily-temperatures/
    - 다음 더 큰 수 찾기 >> stack 역방향 활용 - deque는 FIFO라 역방향, 오른쪽 탐색 기반에 약함
    - Next Greater Element의 대표적인 문제로 꼭 기억!
    - Monotonic Stack (단조 스택)활용 - 인덱스 저장해서 차이 계산 쉽게!
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n  # 결과 배열 초기화
        stack = []  # 인덱스를 저장

        for i in range(n - 1, -1, -1):  # 역방향 탐색
            # 현재보다 작거나 같은 온도는 pop (필요 없음)
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                answer[i] = stack[-1] - i  # 차이만큼 일 수 기록

            stack.append(i)  # 현재 인덱스를 스택에 추가

        return answer
