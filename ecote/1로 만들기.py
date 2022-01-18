# 다이나믹 프로그래밍
# 정수 X가 주어질 때 연산은 4가지이다.
# a) 5로 나누어떨어지면 5로 나눈다.
# b) 3로 나누어떨어지면 3로 나눈다.
# c) 2로 나누어떨어지면 2로 나눈다.
# d) 1을 뺀다.
# 연산 4개를 적절히 사용해서 1을 만드는데 필요한 최소 횟수값을 출력

def solution(N):
    d = [0] * 30001

    for i in range(2, N + 1):
        d[i] = d[i - 1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)

    print(d)
    return d[N]


print(solution(N=26))
