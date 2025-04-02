from collections import Counter
from functools import lru_cache
from bisect import bisect_right


# tag: dynamic_programming, binary_search
class Solution:
    """
    https://leetcode.com/problems/maximum-total-damage-with-spell-casting
    spell[i]를 사용하면 +-1, +-2 power의 spell 사용 못함
    dp(i)는 unique_powers[i]부터 끝까지 고려했을 때의 최대 총 피해량을 반환하는 재귀 함수입니다.
    option1은 현재 주문을 선택하지 않는 경우의 최대 총 피해량입니다.
    option2는 현재 주문을 선택하는 경우의 최대 총 피해량으로, 현재 피해량과 다음으로 선택할 수 있는 주문부터의 최대 총 피해량의 합입니다.
    bisect_right를 사용하여 현재 피해량 + 2보다 큰 첫 번째 요소의 인덱스를 찾아 다음으로 선택할 수 있는 주문의 시작점을 결정합니다
    """

    def maximumTotalDamage(self, power):
        # 피해량의 빈도수를 계산합니다.
        count = Counter(power)
        # 중복을 제거하고 정렬된 피해량 리스트를 생성합니다.
        unique_powers = sorted(count.keys())
        n = len(unique_powers)

        # 메모이제이션을 위한 데코레이터를 사용합니다.
        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0
            current_power = unique_powers[i]
            # 현재 주문을 선택하지 않는 경우
            option1 = dp(i + 1)
            # 현재 주문을 선택하는 경우
            total_damage = current_power * count[current_power]
            # 다음으로 선택할 수 있는 주문의 인덱스를 찾습니다.
            next_index = bisect_right(unique_powers, current_power + 2, i + 1, n)
            option2 = total_damage + dp(next_index)
            return max(option1, option2)

        return dp(0)
