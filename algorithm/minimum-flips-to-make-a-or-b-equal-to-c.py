# tag: bit_manipulation
class Solution:
    """
    https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
    주어진 세 정수 a, b, c에 대해 a | b == c가 되도록 최소 몇 번의 비트 플립이 필요한지 계산하는 문제입니다.
    - flip의 개념 a or b의 bit중 하나를 0>1, 1>0으로 바꾸는 것
    - 최소 flip 수
    - 비트 단위로 변환 후 비교
    """

    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for i in range(32):  # 32비트 정수 기준
            a_bit = (a >> i) & 1  # 비트 단위로 a의 i번째 비트 추출(오른쪽 쉬프트 후 AND 연산) - 쉬프트는 나누는 개념
            b_bit = (b >> i) & 1  # 비트 단위로 b의 i번째 비트 추출
            c_bit = (c >> i) & 1  # 비트 단위로 c의 i번째 비트 추출

            if (a_bit | b_bit) != c_bit:  # OR 연산인데 c의 i번째 비트와 다르면 flip 필요
                if c_bit == 1:
                    flips += 1  # a,b가 둘 다 0이면 하나는 1로
                else:  # c_bit == 0
                    flips += a_bit + b_bit  # 1인 비트만큼 flip

        return flips
