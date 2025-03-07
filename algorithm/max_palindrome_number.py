from collections import Counter

# tag: greedy, Hashing
def largest_palindrome_from_string(s):
    """
    문자열 숫자 N이 주어졌을 때 가장 큰 팰린드롬수를 구하시오 단, 0으로 시작하면 안됨
    Args: s (str): 숫자로 이루어진 문자열

    Returns:
        str: 가장 큰 팰린드롬수
    """
    count = Counter(s)  # 숫자의 빈도수 계산
    valid_digits = [digit for digit in count if digit != '0']  # 0 제외

    if not valid_digits:
        return "0"  # 0을 제외한 숫자가 없으면 유효한 팰린드롬 불가 => 0

    # 1. 가장 큰 숫자로 팰린드롬 구성
    even_pairs = []  # 짝수 개수의 숫자로 양쪽 배치
    odd_digit = None  # 중앙에 올 숫자

    # 숫자를 큰 순서대로 정렬 (내림차순)
    for digit in sorted(valid_digits, reverse=True):
        if count[digit] % 2 == 1 and odd_digit is None:  # 홀수 개인 숫자 하나 선택 (가장 큰 값)
            odd_digit = digit
        even_pairs.extend([digit] * (count[digit] // 2))  # 짝수 개수로 좌우 배치

    # 2. 팰린드롬 조합
    left_half = "".join(even_pairs)  # 왼쪽 절반
    palindrome = left_half + (odd_digit if odd_digit else '') + left_half[::-1]  # 전체 팰린드롬

    # 3. 0으로 시작하면 제외하고 가장 큰 숫자 하나 반환
    if palindrome and palindrome[0] == '0':
        return max(valid_digits)  # 0 제외 후 가장 큰 숫자 반환

    return palindrome

# 테스트 실행
print(largest_palindrome_from_string("00900"))   # 출력: "9"
print(largest_palindrome_from_string("0912"))    # 출력: "9"
print(largest_palindrome_from_string("9876789")) # 출력: "9876789"
print(largest_palindrome_from_string("00"))     # 출력: "0"
print(largest_palindrome_from_string("112233"))  # 출력: "332211"
print(largest_palindrome_from_string("99224488"))  # 출력: "99884499"