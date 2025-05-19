import bisect
from typing import List


# tag: binary_search, sorting, strring
class Solution:
    """
    https://leetcode.com/problems/search-suggestions-system
    - 문자열 접두사(prefix) 탐색
    - 매키 입력마다 사전순대로 최대 3개 추천
    - 사전순 정렬먼저
    - 검색단어로 loop 돌면서 products 접두사 일치하는거 추출 그 중에서 3개만 슬라이싱 - 이러면 성능이슈
        - min으로 bisect loop 3개 길이 제한
    - lambda filter는 느려서 따르게 하려면 binary_search 사용 - bisect!!!
    """

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        prefix = ""
        for c in searchWord:
            prefix += c
            # 이진 탐색으로 현재 prefix의 시작 인덱스 찾기
            start = bisect.bisect_left(products, prefix)
            suggestions = []
            for i in range(start, min(start + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
            result.append(suggestions)
        return result
