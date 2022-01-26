# N * M 직사각형 크기 연구소
# 바이러스는 상하좌우로 인접한 빈칸으로 퍼져나갈 수 있습니다.
# 새로 세울 수 있는 벽의 개수는 3개

# 3개로 세울 수 있는 조합으로 완전 탐색(DFS)한다.
# 벽을 세우고, 바이러스를 퍼지게 한 다음
# '0' 빈칸의 개수를 세어 기록한다.

def solution(n, m, data):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    global result
    result = 0
    temp = [[0 for _ in range(m)] for _ in range(n)]

    # 바이러스가 상하좌우로 퍼지고, 벽을 만날때까지 퍼트린다.
    def virus(x, y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    virus(nx, ny)

    def get_score():
        score = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    score += 1
        return score

    def dfs(count):
        global result
        if count == 3:
            for i in range(n):
                for j in range(m):
                    temp[i][j] = data[i][j]  # 검사하기 위한 데이터 복사

            for i in range(n):
                for j in range(m):
                    if temp[i][j] == 2:
                        virus(i, j)

            result = max(result, get_score())
            return

        else:
            # 3개 벽 완전탐색
            for i in range(n):
                for j in range(m):
                    if data[i][j] == 0:
                        data[i][j] = 1
                        count += 1
                        dfs(count)
                        data[i][j] = 0
                        count -= 1

    dfs(0)
    return result


print(
    solution(n=7, m=7, data=[[2, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 2, 0], [0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]))

print(solution(n=4, m=6, data=[[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 2], [1, 1, 1, 0, 0, 2], [0, 0, 0, 0, 0, 2]]))
print(solution(n=8, m=8, data=[[2, 0, 0, 0, 0, 0, 0, 2],
                               [2, 0, 0, 0, 0, 0, 0, 2],
                               [2, 0, 0, 0, 0, 0, 0, 2],
                               [2, 0, 0, 0, 0, 0, 0, 2],
                               [2, 0, 0, 0, 0, 0, 0, 2],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0]]))
