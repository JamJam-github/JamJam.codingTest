# 빛의 경로 사이클

# 어려워서 못풀었음.

# d는 방향 [아래, 왼쪽, 위, 오른쪽] 순서
# 아래 방향으로 갈때 = [0]일때 [1, 0] 증가
# 왼쪽 방향으로 갈때 = [1]일때 [0, -1] 증가
# 위쪽 방향으로 갈때 = [2]일때 [-1, 0] 증가
# 오른쪽 방향으로 갈때 = [3]일때 [0, 1] 증가
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def dfs(sx, sy, sd, grid):
    global visited
    x, y, d = sx, sy, sd
    count = 0
    visited[sx][sy][sd] = True

    while True:
        count += 1
        # 방문할 새 좌표 계산
        x = (x + dx[d]) % n
        y = (y + dy[d]) % m

        # 좌표 계산 후 다음 d 방향을 계산해주기
        if grid[x][y] == 'R':
            d = (d + 1) % 4
        elif grid[x][y] == 'L':
            d = (d - 1) % 4

        # 방문한 이력이 있으면 그 자리에서 종료
        if visited[x][y][d]:
            if (x, y, d) == (sx, sy, sd):
                return count
            else:
                return 0

        # 새 좌표 방문처리 완료
        visited[x][y][d] = True


# 3차원 배열 [x][y][나가는 방향]
def solution(grid):
    answer = []
    global n, m, visited
    n = len(grid)
    m = len(grid[0])
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    # print(visited)

    # 상하좌우 시작점 1번씩 호출
    for x in range(n):
        for y in range(m):
            for d in range(4):
                if not visited[x][y][d]:
                    res = dfs(sx=x, sy=y, sd=d, grid=grid)
                    if res:
                        answer.append(res)

    answer.sort()
    return answer


print(solution(grid=["SL", "LR"]))
print(solution(grid=["R", "R"]))
