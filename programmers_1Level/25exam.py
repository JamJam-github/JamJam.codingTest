# 소수 만들기
from itertools import combinations


def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    # x가 해당 수로 나누어떨어진다면 소수가 아님
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    # n = len(nums)
    # for i in range(n - 2):
    #     for j in range(i + 1, n - 1):
    #         for k in range(j + 1, n):
    #             x = nums[i] + nums[j] + nums[k]
    #             if is_prime_number(x):
    #                 answer += 1

    for i in combinations(nums, 3):
        # print(i, sum(i))
        if is_prime_number(sum(i)):
            answer += 1
    return answer


print(solution(nums=[1, 2, 7, 6, 4]))
