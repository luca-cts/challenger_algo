# tag: stack, monotonic_stack
class StockSpanner:
    """
    https://leetcode.com/problems/online-stock-span/
    - input stockspanner, next, .. 클래스 init, method 명, 처음에 빈 스택 [], 그다음 100, 80, 60.. 순서대로 stack.append
    - 이전 price값 비교
    - 리턴 - 이전 연속된일수 중에 price보다 작거나 같은 가격이 몇일 연속 되었는가? - span
    - stack = [(price, 연속날수=span)]을 저장해야 될듯??
        - next method는 span=1일 부터 시작하고 최신 stack price가 주어진 price보다 작거나 같은 때 pop
        - pop 한 span sum
    """

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
