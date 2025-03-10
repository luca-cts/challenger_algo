class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# tag: linked_list, math, recursion
class Solution:
    """
    https://leetcode.com/problems/add-two-numbers/description/?envType=problem-list-v2&envId=math
    덧셈 수칙 linked_list element에 적용 올림수 `s//10`, 노드값 `s%10` 계산
    자리수 덧셈은 `linked_list.next = ListNode(s%10)`로 자리수 차례대로 계산
    자리수 이동 while loop로 덧셈 자리가 끝날 때까지
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()  # 결과 리스트의 더미 헤드 (결과 연결 리스트를 만들기 위함)
        current = dummy
        carry = 0  # 자리 올림 저장 변수

        while l1 or l2 or carry:  # 자리수 끝날 때까지 올림 있으면 올림 까지 마무리
            val1 = l1.val if l1 else 0  # l1의 값 (없으면 0)
            val2 = l2.val if l2 else 0  # l2의 값 (없으면 0)

            total = val1 + val2 + carry  # 두 노드 값 + 올림수
            carry = total // 10  # 올림수 계산
            current.next = ListNode(total % 10)  # 자리수 덧셈 - 현재 노드 값 (1의 자리)

            # 다음 자리수로 이동
            current = current.next  # 정답지 ListNode
            if l1:  #  l1 args ListNode
                l1 = l1.next  # type: ignore
            if l2:  # l2 args ListNode
                l2 = l2.next  # type: ignore

        return dummy.next  # 더미 헤드 다음 노드부터 결과 반환


def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


# 입력 리스트
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

# 실행
solution = Solution()
result = solution.addTwoNumbers(l1, l2)  # type: ignore
