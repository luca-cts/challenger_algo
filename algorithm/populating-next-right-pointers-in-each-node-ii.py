from typing import Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# tag: linked_list, binary_tree, bfs
class Solution:
    """
    https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii
    이진 트리의 각 노드에 대해 .next 포인터를 같은 레벨의 오른쪽 노드로 연결하라.
    오른쪽에 노드가 없다면 .next = None.
    in-place로 연결하되, 추가 공간은 O(1) 이어야 함. (재귀 스택은 허용)
    각 레벨의 노드를 current로 순회
    다음 레벨의 노드를 dummy.next로 구성
    .next를 연결하며 새로운 레벨 준비
    다음 반복 때는 current = dummy.next로 다음 레벨로 이동
    """

    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None

        current = root

        while current:
            dummy = Node(0)  # 다음 레벨의 시작 노드를 가리킬 임시 노드
            tail = dummy  # tail은 항상 다음에 연결할 위치

            # 현재 레벨 순회
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                if current.right:
                    tail.next = current.right
                    tail = tail.next

                current = current.next  # 현재 레벨에서 다음 노드로 이동

            # 다음 레벨로 이동
            current = dummy.next

        return root
