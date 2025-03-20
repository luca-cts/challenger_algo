from collections import deque


# tag: queue
def solution(priorities, location):
    """
    https://school.programmers.co.kr/learn/courses/30/lessons/42587

    """
    queue = deque(enumerate(priorities))  # (index, priority) 형태로 큐 생성
    # deque([(0, 2), (1, 1), (2, 3), (3, 2)]) 모양
    order = 0  # 출력되는 순서

    while queue:
        cur = queue.popleft()  # 현재 문서 (index, priority)

        # 현재 문서보다 중요한 문서가 남아있다면 다시 큐에 넣음
        if any(cur[1] < doc[1] for doc in queue):
            queue.append(cur)
            # deque([(1, 1), (2, 3), (3, 2), (0, 2)])
            # deque([ (2, 3), (3, 2), (0, 2), (1, 1)])
            # deque([  (3, 2), (0, 2), (1, 1), (2, 3)])
            # 위의 순서대로 진행됩니다.
        else:
            order += 1  # 인쇄 순서 증가
            if cur[0] == location:  # 내가 찾는 문서라면
                return order  # 몇 번째로 인쇄되는지 반환


# ✅ 테스트 실행
print(solution([2, 1, 3, 2], 2))  # 출력: 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 출력: 5
