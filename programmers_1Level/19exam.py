# 부족한 금액 계산하기


price, money, count, result = 3, 20, 4, 10


def solution(price, money, count):
    total_money = sum([price * i for i in range(1, count + 1)])
    return max(0, total_money-money)


print(solution(price, money, count))
