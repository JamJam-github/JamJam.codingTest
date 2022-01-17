# 메뉴 리뉴얼
# 문제 이해하려면 한세월..........................................

# 1번 손님 주문한 메뉴 'A, B, C, F, G'
# 2번 손님 주문한 메뉴 'A, C'
# 3번 손님 주문한 메뉴 'C, D, E'
# 코스 요리 2개로 구성할때 'A, C'를 4번 주문했다.
# 코스 요리 3개로 구성할때 'C, D, E'를 3번 주문했다.

# 각 손님이 가장 많이 함께 주문한 메뉴들 (2개 이상의) 코스 메뉴로 만든다.
# 최소 2명 이상의 손님으로부터 주문된 메뉴 조합만 포함시킨다.
# 가장 많이 주문한 C개의 조합을 Count해서 Max 값을 찾아 해당 주문 조합을 반환

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for c in course:
        temp = []
        for order in orders:
            # combi = list(combinations(order, c))
            # print(c, '::', list(combinations(order, c)))
            temp += list(combinations(sorted(order), c))

        count = Counter(temp)
        # print('count::', count)

        value = count.values()
        if count and max(value) > 1:
            for i, v in count.items():
                if v == max(value):
                    # print(i, v)
                    answer.append(''.join(i))
    return sorted(answer)


print(solution(orders=["XYZ", "XWY", "WXA"],
               course=[2, 3, 4]))

import math
def calcManhattanDist(x, y):
    sum = 0
    for i, j in zip(x, y):
        sum += math.abs(i-j)

