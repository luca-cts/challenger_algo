from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# tag: linked_list, two_pointers
class Solution:
    """
    https://leetcode.com/problems/partition-list/
    - 두 개의 연결 리스트(`less`, `greater`)를 만들어 노드를 구분
    - 기준값(`x`)보다 작은 노드는 `less` 리스트에 추가
    - 기준값(`x`) 이상인 노드는 `greater` 리스트에 추가
    - 두 리스트를 연결하여 최종 결과 반환
    """

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = less_tail = ListNode(0)  # x보다 작은 노드 저장용 더미 노드
        greater_head = greater_tail = ListNode(0)  # x 이상 노드 저장용 더미 노드

        while head:
            if head.val < x:
                less_tail.next = head  # x보다 작은 노드 추가
                less_tail = less_tail.next
            else:
                greater_tail.next = head  # x 이상 노드 추가
                greater_tail = greater_tail.next
            head = head.next  # 다음 노드로 이동

        greater_tail.next = None  # 마지막 노드의 next를 None으로 설정
        less_tail.next = greater_head.next  # 두 리스트 연결

        return less_head.next  # 새로운 리스트의 시작 노드 반환


def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


def print_linked_list(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print(" -> ".join(result))


head = create_linked_list([1, 4, 3, 2, 5, 2])
x = 3

result = Solution().partition(head, x)
print_linked_list(result)  # 출력: "1 -> 2 -> 2 -> 4 -> 3 -> 5"
