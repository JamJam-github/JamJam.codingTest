# 완전탐색 > 소수 찾기

from itertools import permutations


# 소수방법1)
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(x ** 0.5) + 1):
        # x가 해당 수로 나누어떨어진다면 소수가 아님
        if x % i == 0:
            # print(x, '는', i, '로 떨어진다.')
            return False
    return True


def solution(numbers):
    dic = {}
    nums = [i for i in numbers]
    # print(nums)

    # 순열로 데이터를 찾은 후 해당 데이터를 문자열로 join 합친다.

    nPr = []
    for i in range(1, len(nums) + 1):
        nPr += list(map(''.join, permutations(nums, i)))
    # print('순열', nPr)

    for i in nPr:
        n = int(i)
        if n > 1 and is_prime_number(n):
            dic[n] = 1

    # print('dic::', dic)
    # nCr = list(itertools.combinations(nums, len(nums)))
    # print('조합', nCr)
    return len(dic)


# print(solution(numbers="7843"))
# print(solution(numbers="011"))


# 다른 사람의 풀이
def solution_other(n):
    a = set()

    # s = {}은 dict 타입, s = set()은 set 타입
    # 합집합 '|' 사용
    # 교집합 '&' 사용
    # 차집합 '-' 사용, 대칭차집합(합집합-교집합) '^'
    # 연산과 동시에 할당하기 위해 '|=', '-=' 사용
    # 소수가 아닌 range 0 ~ 2를 현재 set에서 제거해주기
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    print('current::', a)
    a -= set(range(0, 2))

    # 소수 방법2) 에라토스테네스의 체 - 범위에서 합성수를 지우는 방식으로 소수를 찾는 방법
    # 2부터 제곱근까지 확인하면서 i*2에서 제곱근까지 범위 중 i배수를 모두 지운다.
    # for i in range(2, n+1):
    #   for j in range(i*2, n+1, i):
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))

    return len(a)


print(solution_other(n='011'))
