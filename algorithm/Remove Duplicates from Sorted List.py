from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# tag: linked_list
class Solution:
    """
    https://leetcode.com/problems/remove-duplicates-from-sorted-list/
    - 정렬된 linked list에서 중복된 노드를 제거하는 문제
    - current.val == current.next.val 이면 current.next를 건너뛴다
    """

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # skip duplicate
            else:
                current = current.next  # move forward

        return head
