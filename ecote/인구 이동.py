# DFS
# N * N 크기의 각 땅에는 A[r][c]명이 살고 있습니다.
# 국경선을 공유하는 두 나라의 인구차이 L명 이상, R명 이하라면 국경선을 엽니다.
# 연합을 이루고 있는 인구수는 (연합의 인구수) / (연합 개수)
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

n = 4
l, r = 10, 50
data = [[10, 100, 20, 90],
        [80, 100, 60, 70],
        [70, 20, 30, 40],
        [50, 20, 100, 10]]


def bfs(a, b, data, visited):
    unit = []  # 연합된 나라 좌표

    queue = deque()
    queue.append((a, b))

    unit.append((a, b))
    people = data[a][b]  # 인구 합산
    visited[a][b] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(data[nx][ny] - data[x][y]) <= r:
                    queue.append((nx, ny))
                    unit.append((nx, ny))
                    people += data[nx][ny]
                    visited[nx][ny] = True

    unionPeople = people // len(unit)

    for i, j in unit:
        data[i][j] = unionPeople
    
    # 연합된 국가가 1개(자기 자신)인 경우 False
    return True if len(unit) >= 2 else False


def solution(n, l, r, data):
    total_count = 0

    # visited 초기화해서 인구이동을 할 수 없을 때까지 반복한다.
    while True:
        visited = [[False for _ in range(n)] for _ in range(n)]
        stop = True  # stop이 True면 while문 종료

        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    check = bfs(i, j, data, visited)
                    # print((i, j), '좌표의 결과::', check)

                    # n * n 모두 자기 자신밖에 없을 경우 true로 유지되어 break
                    if check:
                        stop = False

        # print('-----total count::', total_count, 'stop 결과 ::', stop)
        if stop:
            break
        else:
            total_count += 1
    return total_count


print(solution(n, l, r, data))
