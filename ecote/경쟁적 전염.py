# BFS 문제
# K개의 바이러스가 낮은 번호부터 증식한다.
from collections import deque


def solution(n, k, graph, s, x, y):
    res_x, res_y = x - 1, y - 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    data = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                data.append((graph[i][j], 0, i, j))  # (바이러스, 시간, x좌표, y좌표)

    queue = deque(data)
    while queue:
        virus, sec, x, y = queue.popleft()

        if s == sec:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus
                    queue.append((virus, sec + 1, nx, ny))

    # print(graph)
    return graph[res_x][res_y]


print(solution(n=3, k=3, graph=[[1, 0, 2], [0, 0, 0], [3, 0, 0]], s=2, x=3, y=2))
