from typing import List


# tag: stack, math
class Solution:
    """
    https://leetcode.com/problems/evaluate-reverse-polish-notation/
    후위 표기법
    2 + 3 - 중위 표기법
    2 3 + 후위 표기법
    나머지 사칙연산 순서는 동일
    나눗셈은 소수점 버리고 0 방향으로 내림(truncate toward zero)
    """

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # 트렁크 나눗셈 (0 방향으로 내림)
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]
