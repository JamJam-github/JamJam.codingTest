# 5와 사칙연산만으로 12를 표현할 수 있습니다.
from collections import deque


def solution(N, number):
    answer = float('inf')
    if N == number:
        return 1

    def oper(n1, n2, p):
        if p == '-':
            res = int(n1) - int(n2)
        elif p == '+':
            res = int(n1) + int(n2)
        elif p == '*':
            res = int(n1) * int(n2)
        else:
            res = int(n1) // int(n2)
        return res

    queue = deque()
    queue.append((0, 0))

    while queue:
        count, value = queue.popleft()

        if count > 8:
            continue

        if value == number:
            answer = min(answer, count)
            continue

        count += 1
        for i in range(8):
            nn = int(str(N) * (i+1))
            queue.append((count+i, oper(value, nn, '+')))
            queue.append((count+i, oper(value, nn, '-')))
            queue.append((count+i, oper(value, nn, '*')))
            queue.append((count+i, oper(value, nn, '/')))

    return -1 if answer > 8 else answer


# print(solution(N=5, number=12))
# print(solution(N=2, number=11))
print(solution(N=5, number=5))

