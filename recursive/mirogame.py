# 미로 탈출
# N * M 크기의 직사각형 형태의 미로에서
# 현재 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치
# 괴물이 있는 부분은 0, 없는 부분은 1로 표시되어 있다.
# 탈출하기 위해 움직여야 하는 최소 칸의 개수
graph = [[1, 0, 1, 0, 1, 0],
         [1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1]]

graph = [[1, 1, 0, 0],
         [1, 0, 0, 1],
         [1, 1, 1, 1]]

n, m = 3, 4

graph = [[1, 0, 1, 1, 1],
         [1, 0, 1, 0, 1],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 0, 1],
         [0, 0, 0, 0, 1]]
n, m = 5, 5

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque


def bfs(x, y):
    queue = deque()
    # 첫 시작점을 큐에 넣음
    queue.append((x, y))

    while queue:
        # 큐에서 기준점을 꺼내오기
        x, y = queue.popleft()

        # 상하좌우 확인해서
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간을 벗어날 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽의 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 처음 방문하는 경우만 1이며, 해당 좌표에 최단 거리를 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    for i in range(n):
        for j in range(m):
            print(graph[i][j], end=' ')
        print()
    # 가장 아래의 오른쪽에 최단 거리가 기록되있을 것이며, 반환
    return graph[n - 1][m - 1]


print(bfs(0, 0))
