# 가장 큰 수
# 정수를 이어 붙여 만들 수 있는 가장 큰 수

# 문자열 비교는 첫번째 인덱스 값으로 비교한다.

# 순열 사용시 시간초과
# from itertools import permutations
# 
# def solution_(numbers):
#     numbers = list(map(str, numbers))
#     nPr = list(permutations(numbers))
#     result = []
#     for n in nPr:
#         result.append("".join(n))
#     return max(result)

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))


print(solution(numbers=[3, 30, 34, 5, 9]))
print(solution(numbers=[0, 0]))

# 다른 풀이
# 커스텀 정렬
import functools


def comparator(a, b):
    # a가 크면 1, b가 크면 -1, a와 b가 동일하면 0 리턴하면 정렬된다.
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))


def solution_other(numbers):
    n = [str(x) for x in numbers]
    # sorted 함수의 key 매개변수에 특별한 방법으로 소트를 할 수 있는 함수
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer
