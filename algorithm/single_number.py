from typing import List


# tag: bit_manipulation
class Solution:
    """
    https://leetcode.com/problems/single-number
    - XOR 비트 연산을 이용한 풀이
    - XOR 연산의 성질: a ^ a = 0, a ^ 0 = a
    - 모든 숫자를 XOR 연산하면 중복된 숫자는 0이 되고, 남은 숫자가 유일한 숫자
    """

    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
