# 동적계획법 DP
# 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다.
# 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.
# m = 4, n = 3 인 경우입니다.
# 집이 있는 곳의 좌표는 (1, 1)로 나타내고
# 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.

# 격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다.
# 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를
# 1,000,000,007로 나눈 나머지를 return

def solution(m, n, puddles):
    # 왼쪽, 위로 한줄씩 만들어서 IndexError 방지
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    # 집
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j == 1:
                continue

            # 웅덩이는 0으로 만들어 다음 덧셈 때 영향끼치지 않게
            if [j, i] in puddles:
                dp[i][j] = 0
                continue

            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    # 가장 아래의 오른쪽
    return dp[n][m]


print(solution(m=4, n=3, puddles=[[2, 2]]))
