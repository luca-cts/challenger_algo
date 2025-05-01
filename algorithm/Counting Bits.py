from typing import List


# tag: bit_manipulation, dp
class Solution:
    """
    https://leetcode.com/problems/counting-bits
    - n = 0 ~ n까지의 숫자에서 bit의 1의 개수의 리스트를 반환
    - format(n, "b")로 2진수 변환 후 count("1")로 1의 개수 세기
    """

    def countBits(self, n: int) -> List[int]:
        return [format(i, "b").count("1") for i in range(n + 1)]
