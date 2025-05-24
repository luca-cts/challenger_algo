from typing import List


# tag: dynamic_programming
class Solution:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
    - 매일 주식 가격, 거래수수료
    - 주식 사고파는건 하루에 한번씩만, 그리고 1번에 1주만 보유가능
    - dp 문제 - 현재 가지고 있는 현금이냐, 주식을 사서 주식 가치 상승을 노리느냐 둘 중 머가 max일까?
    - 현금 흐름
        - 유지하거나 고점 주식 팔기
    - 주식 흐름
        - 오르길 기다리거나 저점 매수 하기
    """

    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        cash = 0  # 주식을 보유하지 않은 상태에서의 최대 이익
        hold = -prices[0]  # 주식을 보유한 상태에서의 최대 이익 (첫 날 구매 가정)

        print(f"Day 0: price={prices[0]}, cash={cash}, hold={hold}")

        for i in range(1, n):
            prev_cash = cash
            prev_hold = hold

            # 현금 상태: 이전 cash 유지 or 주식 매도
            cash = max(prev_cash, prev_hold + prices[i] - fee)
            # 보유 상태: 이전 hold 유지 or 새 주식 매수
            hold = max(prev_hold, prev_cash - prices[i])

            print(f"Day {i}: price={prices[i]}, cash={cash}, hold={hold}")

        return cash
