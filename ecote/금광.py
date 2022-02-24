# 다이나믹 프로그래밍
# m 번에 걸쳐 얻을 수 있는 금의 최대 크기
# 맨 처음에는 첫 번째 열의 어느 행에서든 출발 가능

# 1열부터 0열의 왼쪽위, 왼쪽, 왼쪽아래 데이터 중 큰 값을 더한다. (반복)
# 최종적으로 m-1열의 데이터 중 큰 값을 리턴한다.


def solution(n, m, data):
    dp = data[:]

    # i=n행, j=m 열
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]

            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]

            dp[i][j] = dp[i][j] + max(left_up, left_down, dp[i][j - 1])

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    # for d in dp:
    #     print(d)
    return result


print(solution(n=3, m=4, data=[[1, 3, 3, 2], [2, 1, 4, 1], [0, 6, 4, 7]]))
