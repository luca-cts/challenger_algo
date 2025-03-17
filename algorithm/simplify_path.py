# tag: stack, string
class Solution:
    """
    https://leetcode.com/problems/simplify-path/description/
    - 문자열을 `'/'` 기준으로 분할
    - `".."`이면 부모 디렉토리로! - 갈려면 가장 최근에 입력된거 디렉토리 제거하면`pop()`
    - `"."`과 `""`(빈 값)는 무시
    - 그 외는 `append()`
    """

    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")  # '/' 기준으로 나누기

        for part in parts:
            if part == "..":  # 이전 디렉토리로 이동
                if stack:
                    stack.pop()
            elif part and part != ".":  # 빈 문자열("") 및 "." 무시
                stack.append(part)

        return "/" + "/".join(stack)  # 최종 경로 생성
