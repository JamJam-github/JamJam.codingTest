# 위장

# 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return

# 각 경우의 수를 모두 곱해라.

from collections import defaultdict

def solution(clothes):
    answer = 1
    hash = defaultdict(list)
    for i, j in clothes:
        hash[j].append(i)
    # print(hash)

    for i in hash.values():
        answer *= (len(i) + 1)

    return answer - 1


print(solution(clothes=[["yellowhat", "headgear"],
                        ["bluesunglasses", "eyewear"],
                        ["green_turban", "headgear"]]))
print(solution(clothes=[["crowmask", "face"],
                        ["bluesunglasses", "face"],
                        ["smoky_makeup", "face"]]))
