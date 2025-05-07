from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# tag: linked_list, pointers, recursion
class Solution:
    """
    https://leetcode.com/problems/reverse-linked-list
    - 링크드 리스트 뒤집기
    - 헤더 노드의 next 방향을 반대로(previous) 바꾸는 걸 링크드 리스트 끝날때 까지 반복
    - prev_node: 이전 노드
    - cur_node: 현재 노드
    - next_node: 다음 노드
    - next_node = cur_node.next 저장한 뒤 cur_node.next = prev_node로 방향을 바꿔줌
    - prev_node = cur_node로 현재 노드를 이전 노드로 바꿔주고, cur_node = next_node로 다음 노드로 이동 반복
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        cur_node = head
        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        return prev_node
