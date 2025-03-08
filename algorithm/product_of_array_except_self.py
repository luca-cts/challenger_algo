from typing import List


# tag: array, prefix_sum
class Solution:
    """
    https://leetcode.com/problems/product-of-array-except-self/description/
    self index value를 제외한 나머지 element들의 곱을 구하는 문제
    Args: nums (List[int]): 숫자 배열
    Returns: List[int]: 숫자배
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products = [1] * length  # 배열 초기값
        for i in range(1, length):
            products[i] = (
                products[i - 1] * nums[i - 1]
            )  # 자신을 기준으로 왼쪽 엘레멘트 곱

        reverse = nums[-1]  # 가장 오른쪽 엘레멘트는 곱할 필요 없음
        for i in range(length - 2, -1, -1):
            products[i] *= reverse  # 자신 기준 오른쪽 엘레멘트 곱
            reverse *= nums[i]  # 누적 곱값
        return products
