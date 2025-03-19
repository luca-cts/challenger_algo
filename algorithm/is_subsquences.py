# tag: string, two_pointers, dynamic_programming
class Solution:
    """
    https://leetcode.com/problems/is-subsequence/description/
    s 문자열이 t 문자열의 subsequence인지 확인하는 문제 (문자열 순서만 맞으면 됨)
    Args:
        s (str): 문자열
        t (str): 문자열
    Returns:
        bool: s 문자열이 t 문자열의 subsequence인지 여부
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0  # two-pointer
        while i < len(s) and j < len(t):  # 2개 list 동시에
            if s[i] == t[j]:  # t에서 s letter 순서대로!
                i += 1  #  t에서 s의 순서대로 추출(추출은 len의 증가)
            j += 1  # t는 계속 loop
        return i == len(s)
