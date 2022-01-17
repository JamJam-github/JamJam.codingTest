# 나머지가 1이 되는 수 찾기
# x는 (n-1)을 기준으로
# x가 짝수면 n(홀수)을 짝수로 나눌 경우 항상 1이 남는다.
# x가 홀수면 n(짝수)는 x로 나눠지는 약수로 나눌 경우 항상 1이 남는다.
import math


def solution(n):
    x = n - 1
    if x % 2 == 0:
        return 2
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return i
    return x


print(solution(1000000))


# 다른 사람의 풀이
def solution(n):
    answer = min([x for x in range(1, n+1) if n % x == 1])
    return answer