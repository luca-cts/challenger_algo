from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# tag: linked_list, two_pointers
class Solution:
    """
    https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list
    - 연결 리스트를 배열에 변환
    - 양 끝에서부터 쌍으로 합 계산
    - 최댓값 갱신
    """

    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        while head:
            vals.append(head.val)  # 배열반환
            head = head.next

        max_sum = 0
        n = len(vals)
        for i in range(n // 2):  # 양끝에서부터 쌍으로 합 계산 -> <-
            max_sum = max(max_sum, vals[i] + vals[n - 1 - i])

        return max_sum
