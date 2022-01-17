from collections import deque

# 위 아래 왼쪽 오른쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    queue = deque()
    # 첫 시작점(0행, 0열)을 큐에 넣음
    queue.append((0, 0))

    while queue:
        # 큐에서 기준점을 꺼내오기
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간을 벗어날 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽의 경우 무시
            if maps[nx][ny] == 0:
                continue

            # 처음 방문하는 경우만 1이며, 해당 좌표에 최단 거리를 기록
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    # 가장 아래의 오른쪽에 최단 거리가 기록되있을 것이며, 반환
    answer = maps[n - 1][m - 1]
    return answer if answer != 1 else -1


print(solution(maps=[[1, 0, 1, 1, 1],
                     [1, 0, 1, 0, 1],
                     [1, 0, 1, 1, 1],
                     [1, 1, 1, 0, 1],
                     [0, 0, 0, 0, 1]]))
print(solution(maps=[[1, 0, 1, 1, 1],
                     [1, 0, 1, 0, 1],
                     [1, 0, 1, 1, 1],
                     [1, 1, 1, 0, 0],
                     [0, 0, 0, 0, 1]]))
