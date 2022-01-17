# 주식가격
from collections import deque


def solution(prices):
    answer = [0] * len(prices)
    n = len(prices)
    for i in range(n):
        start = prices[i]
        for j in range(i + 1, n):

            answer[i] += 1
            if start > prices[j]:
                # print(start, '기준으로', prices[j], '는 작다')
                break
            # print(start, '기준으로', prices[j], '는 크다')

    return answer


print(solution(prices=[1, 2, 3, 2, 3]))


# Queue

def solution_queue(prices):
    answer = []
    queue = deque(prices)

    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break
        answer.append(sec)
    return answer


print(solution_queue(prices=[1, 2, 3, 2, 3]))


# Stack
# answer 배열을 가격이 떨어지지 않은 기간 max 배열로 만든 후
# 스택에 초기 인덱스를 시작으로 떨어지는 구간을 만나면 해당 값으로 변경해주기
def solution_stack(prices):
    n = len(prices)
    answer = [i for i in range(n - 1, -1, -1)]

    stack = [0]
    for i in range(1, n):
        while stack and prices[stack[-1]] > prices[i]:
            index = stack.pop()
            answer[index] = i - index
        stack.append(i)

    return answer


print(solution_stack(prices=[1, 2, 3, 2, 3]))
