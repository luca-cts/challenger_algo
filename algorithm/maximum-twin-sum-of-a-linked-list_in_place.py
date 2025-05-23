from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# tag: linked_list, two_pointers
class Solution:
    """
    https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list
    → 리스트 반 나누고, 뒤쪽 반을 reverse, 앞과 뒷부분을 한 번에 비교 - 최적화된 방법
    - slow/fast 포인터로 중간까지 이동
    - 뒤쪽 리스트를 reverse
    - 앞/뒤를 함께 순회하며 twin sum 계산
    - 최대값 갱신
    """

    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Step 3: twin sum 계산
        max_sum = 0
        first, second = head, prev
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum
