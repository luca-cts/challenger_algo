from collections import deque
from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


# tag: bfs, hash_table, tree
class Solution:
    """
    https://leetcode.com/problems/employee-importance/
    subordinate를 계속 추적해야됨 - 단일 loop로 못 품고 bfs로 풀어야됨
    employees를 dict로 미리 매핑하고, BFS subordinate ids를 따라가면서 importance를 합산해야 한다.
    탐색을 계속 이어가야 한다 => BFS!!
    """

    def getImportance(self, employees: List["Employee"], id: int) -> int:
        dict_em = {em.id: em for em in employees}  # O(n)으로 employees를 dict로 매핑해서 deque 가볍게
        result = 0
        queue = deque([id])  # targer id를 deque에 넣고 시작
        while queue:
            cur_id = queue.popleft()
            employee = dict_em[cur_id]  # target id로 Employee를 찾고
            result += employee.importance  # importance를 더하고
            for sub in employee.subordinates:
                queue.append(sub)  # subordinates를 queue에 넣는다

        return result
