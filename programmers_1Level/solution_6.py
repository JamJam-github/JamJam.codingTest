# x만큼 간격이 있는 n개의 숫자


def solution(x, n):
    answer = []
    for i in range(n):
        if i == 0:
            answer.append(x)
        else:
            answer.append(answer[i - 1] + x)
    return answer


x, n = -4, 3
print(solution(x, n))

# 다른 사람의 풀이
# return [i * x + x for i in range(n)]
