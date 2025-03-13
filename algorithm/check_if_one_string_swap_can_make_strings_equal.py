# tag: hash_table, string, counting
class Solution:
    """
    https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
    - 조건: 한개의 스트링을 스왑했을 때 일치할 경우에 true
    - 2개의 true조건 나머지 false
    s1 == s2 -> true
    if s1 != s2 count 2
        s2 mismatch index swab
            s1 == swab_s2 -> true
    remainder case false

    ab
    ca 의 경우
    and s1[diff_index[0]] == s2[diff_index[1]] a == a true
    and s1[diff_index[1]] == s2[diff_index[0]] b != c false
    """

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        diff_index = [i for i in range(len(s1)) if s1[i] != s2[i]]

        return (
            len(diff_index) == 2
            and s1[diff_index[0]] == s2[diff_index[1]]
            and s1[diff_index[1]] == s2[diff_index[0]]
        )
