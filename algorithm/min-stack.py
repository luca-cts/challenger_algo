# tag: stack
class MinStack:
    """
    https://leetcode.com/problems/min-stack
    단순한 스택 1개로는 최소값 추적이 어렵다.
    그래서 최솟값을 별도로 저장하는 보조 스택(min_stack)을 사용한다.
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []  # 최소값을 저장하는 보조 스택

    def push(self, val: int) -> None:
        self.stack.append(val)
        # min_stack에 현재까지의 최소값을 함께 저장
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
