# 문자열을 정수로 바꾸기


s = "-1234"


def solution(s):
    return int(s)


# 다른 사람의 풀이
# 문자열을 뒤집어서 "결과 += 숫자 * (10 ** 제곱수)"로 풀어나간다.


# 소수 찾기
n = 7843


# 1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(x ** 0.5) + 1):
        # print(x, '는', i, '로 떨어지나?')
        # x가 해당 수로 나누어떨어진다면 소수가 아님
        if x % i == 0:
            return False
    return True


answer = 0
for i in range(2, n + 1):
    if is_prime_number(i):
        print(f'{i}는 소수다.')
        answer += 1

print('정답', answer, '개')
