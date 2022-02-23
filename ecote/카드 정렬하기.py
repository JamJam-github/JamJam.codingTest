# 두 묶음의 카드를 합쳐서 하나로 만들기 위한 최소한의 비교 수를 구하라

def solution(data):
    n = len(data)
    if n <= 2:
        return sum(data)

    data.sort()
    answer = data[0] + data[1]
    total = answer
    for i in range(2, n):
        answer += total + data[i]
        total += data[i]

    return answer


import heapq


def solution2(data):
    answer = 0
    n = len(data)
    heap = []
    for i in range(n):
        heapq.heappush(heap, data[i])

    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        sum_value = n1 + n2
        answer += sum_value
        heapq.heappush(heap, sum_value)

    return answer


print(solution2(data=[10, 20, 40]))
