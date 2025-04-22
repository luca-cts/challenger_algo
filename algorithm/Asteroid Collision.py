# tag: stack, simulation
def asteroidCollision(asteroids):
    """
    https://leetcode.com/problems/asteroid-collision/
    이전 상태 기억, 충돌 후 변화 상태 기억 -> stack 사용

    """
    stack = []  ## stack 문제
    for ast in asteroids:
        while stack and ast < 0 < stack[-1]:  ## stack recursion loop
            if stack[-1] < -ast:
                stack.pop()
                continue  ## 계속 충돌 시킴 -> stack and ast < 0 < stack[-1]
            elif stack[-1] == -ast:
                stack.pop()
            break  ## 충돌 끝 -> for 문으로
        else:  #  stack and ast < 0 < stack[-1] 조건 아니면 오는 분기점
            stack.append(ast)
    return stack


example = [5, 10, -5]
print(asteroidCollision(example))  # Output: [5, 10]
