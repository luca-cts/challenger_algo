from typing import List


# tag: bit_manipulation
class Solution:
    """
    https://leetcode.com/problems/single-number-ii
    모든 비트 자리(0~31)에 대해 "1이 몇 번 등장했는지 세기"
    어떤 비트에서 1이 3의 배수로 등장했다면 → 그 비트는 사라져야 함
    오직 한 번 등장한 숫자만 남게 됨
    nums에서 해당 비트가 켜져 있는 숫자를 센다 -> 총 합을 3으로 나눔 → 나머지가 1이면 정답 숫자가 가진 비트
    """

    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for i in range(32):  # 32비트 정수
            bit_sum = 0
            for num in nums:
                # Python은 음수를 2의 보수로 저장하므로 32비트로 제한
                if (num >> i) & 1:
                    bit_sum += 1
            if bit_sum % 3 != 0:
                result |= 1 << i

        # 음수 보정
        if result >= 2**31:
            result -= 2**32

        return result
