# x가 등장하는 횟수를 계산하세요.
# O(logN)으로 설계
from bisect import bisect_left, bisect_right


def count_by_range(data, x):
    start = bisect_left(data, x)
    end = bisect_right(data, x)
    return end - start


def solution(n, x, data):
    answer = count_by_range(data, x)
    return answer if answer else -1


print(solution(n=7, x=2, data=[1, 1, 2, 2, 2, 2, 3]))
print(solution(n=7, x=4, data=[1, 1, 2, 2, 2, 2, 3]))
