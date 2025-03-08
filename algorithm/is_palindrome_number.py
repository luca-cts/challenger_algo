# tag: math, two_pointers
def is_palindrome_number(n: int):
    """
    주어진 숫자가 팰린드롬인지 확인하시오
    Args:
        n (int): n > 0 이상 자연수

    Returns:
        bool: n이 팰린드롬인지 여부
    """
    if n < 0 or (n % 10 == 0 and n != 0):  # 음수 또는 0이 아닌데 끝이 0이면 False
        return False

    reversed_half = 0
    while n > reversed_half:
        reversed_half = reversed_half * 10 + n % 10  # 마지막 자릿수를 뒤로 추가
        n //= 10  # 맨 끝 자릿수 제거

    return n == reversed_half or n == reversed_half // 10  # 짝수/홀수 자리 대응


# 테스트
print(is_palindrome_number(121))  # True
print(is_palindrome_number(-121))  # False
print(is_palindrome_number(123))  # False
print(is_palindrome_number(1221))  # True
