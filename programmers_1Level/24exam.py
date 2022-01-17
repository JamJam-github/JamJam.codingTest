# 예산
# 물품을 구매해 줄 때는 각 부서가 신청한 금액만큼을 모두 지원해 줘야 합니다.
# 부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때,
# 최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록 solution 함수를 완성해주세요.
from itertools import combinations


def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    for i in range(len(d) - 1, 0, -1):
        l = list(combinations(d, i))
        s = [i for i in l if sum(i) == budget]
        if s:
            return i


# print(solution(d=[1, 3, 2, 5, 4], budget=9))


# 조합 공부
l = [1, 2, 3, 4]
n = 4  # 4개 데이터에서 k(2개:변수필요) 뽑기


def test1():
    for i in range(n - 1):
        for j in range(i + 1, n):
            print(f'({l[i]},{l[j]})')


l = [1, 2, 3, 4, 5]
n = 5  # n(5개) 데이터에서 k(3개:변수필요) 뽑기


def test2():
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                print(f'({l[i]},{l[j]},{l[k]})')
                # for f in range(k + 1, n):
                # print(f'({l[i]},{l[j]},{l[k]},{l[f]})')


# 뽑을 개수가 늘어나면 재귀를 이용하자.
# [0,1,2,3,4]
A = [1, 2, 3, 4, 10]
n, k = 5, 4
arr = [0] * k


def combi(level, s):
    # 종료조건 : 뽑는 k 수가 되면 종료
    if level == k:
        print("LEVEL 다 채워져서 종료::", arr)
        return

    # N=5 개에서 K=3 개 뽑는 경우를 기준으로
    # 5C3 = N! / (N-R)! * R! = 10개의 조합
    # LEVEL 0: 배열에 1개 추가하여 0, 1, 2번째 번호를 첫번째 자리 숫자로 사용할 수 있음.
    # LEVEL 1: 배열에 1개 추가하여 현재 총 2개로, 1, 2, 3번째 번호를 두번째 자리수로 조합 가능
    # LEVEL 2: 배열에 1개 추가하여 총 3개가 완료되고 2, 3, 4번째 번호를 세번째 자리수로 조합 가능

    # N = 5, K = 3, LEVEL = 0, S = S ~ 2(N-K+LEVEL)
    # N = 5, K = 3, LEVEL = 1, S = S ~ 3(N-K+LEVEL)
    # N = 5, K = 3, LEVEL = 2, S = S ~ 4(N-K+LEVEL)

    for i in range(s, n - k + level + 1):
        arr[level] = A[i]
        combi(level + 1, i + 1)


# combi(0, 0)


def solution(d, budget):
    if sum(d) <= budget:
        return len(d)

    d.sort()
    print(d)
    for i in range(len(d)):
        budget -= d[i]

        print(f'현재 budget = {budget}')
        if budget == 0:
            return i + 1
        elif budget < 0:
            return i

    if budget:
        return len(d)


print(solution(d=[1, 3, 2, 5, 4], budget=9))
