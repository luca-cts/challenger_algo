def solution(numbers, target):
    """
    https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
    +-모두 고려해서 함수 작성, 루트에서 끝까지 딥 노드트리 결과물 찾는 것! -> dfs!!!
    - 재귀 함수를 사용해 각 숫자에 대해 두 가지 선택(+와 -)을 진행합니다.:
    - `dfs(i, current_sum)` 함수는 `i`번째 숫자부터 시작하여 현재까지의 누적 합이 `current_sum`인 상태를 나타냅니다.
    - 기저 조건은 모든 숫자를 처리한 경우(`i == len(numbers)`)이며, 이때 누적 합이 `target`과 일치하면 경우의 수(`count`)를 증가시킵니다.
    - 현재 숫자 `numbers[i]`를 더하는 경우와 빼는 경우 두 가지로 분기하여 `dfs(i + 1, current_sum + numbers[i])`와 `dfs(i + 1, current_sum - numbers[i])`를 호출합니다.
    - 이 과정을 재귀적으로 진행하면서 모든 경우의 수를 탐색합니다.
    """
    count = 0  # 외부 함수에 정의된 변수

    def dfs(i, current_sum):
        nonlocal count  # 외부의 count 변수를 사용하겠다고 명시 아니면 nonlocal bound error 남!
        if i == len(numbers):
            if current_sum == target:
                count += 1  # 외부 변수 count를 수정
            return
        dfs(i + 1, current_sum + numbers[i])  # +
        dfs(i + 1, current_sum - numbers[i])  # -

    dfs(0, 0)
    return count
