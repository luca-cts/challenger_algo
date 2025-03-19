from typing import List


# tag: two_pointers, stack, greedy
class Solution:
    """
    https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
    - 왼쪽에서 오른쪽 (`l` 찾기)
        - 단조 증가 스택을 사용하여 정렬이 깨지는 첫 번째 인덱스를 찾음.
        - `nums[i]`보다 큰 값을 만나면, 해당 인덱스를 `pop()`하고 `l`을 최소값으로 갱신.
    - 오른쪽에서 왼쪽 (`u` 찾기)
        - 단조 감소 스택을 사용하여 정렬이 깨지는 마지막 인덱스를 찾음.
        - `nums[i]`보다 작은 값을 만나면, 해당 인덱스를 `pop()`하고 `u`를 최대값으로 갱신.
    - 이미 정렬된 경우 체크
        - `l >= u`이면 정렬이 필요 없으므로 `0` 반환.
        - 그렇지 않으면 `u - l + 1`을 반환하여 정렬이 필요한 부분 배열의 길이를 출력.
    """

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l, u = len(nums) - 1, 0
        stack = []

        # 🔹 (1) 왼쪽에서 오른쪽으로 탐색하여 l 찾기 (단조 증가 스택)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:  # 정렬이 깨지는 지점 찾기
                l = min(l, stack.pop())  # 최소 인덱스 갱신
            stack.append(i)  # 현재 인덱스 추가

        stack = []

        # 🔹 (2) 오른쪽에서 왼쪽으로 탐색하여 u 찾기 (단조 감소 스택)
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:  # 정렬이 깨지는 지점 찾기
                u = max(u, stack.pop())  # 최대 인덱스 갱신
            stack.append(i)  # 현재 인덱스 추가

        # 🔹 (3) 이미 정렬된 경우 체크
        return 0 if l >= u else u - l + 1
