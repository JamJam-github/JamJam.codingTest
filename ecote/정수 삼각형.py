# 정수 삼각형 모양에서 맨 위층부터 시작해서
# 하나를 선택하여 합이 최대가 되는 경우를 구하라.
# 아래층의 수는 현재 층에서 대각선 왼쪽, 대각선 오른쪽만 선택 가능하다.

def solution(n, dp):
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]

            if i == j:
                dp[i][j] += dp[i - 1][i - 1]
            else:
                dp[i][j] += max(left_up, dp[i - 1][j])

    return max(dp[n - 1])


print(solution(n=5, dp=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
