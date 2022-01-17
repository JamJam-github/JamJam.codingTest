# 예상 대진표
import math


def solution(n, a, b):
    answer = 0
    while a != b:
        answer += 1
        a, b = math.ceil(a / 2), math.ceil(b / 2)
    return answer


print(solution(n=8, a=4, b=7))
