# 경주로 부지는 N x N 크기의 정사각형 격자 형태이며 각 격자는 1 x 1 크기입니다.
# 0은 칸이 비어 있음을 1은 해당 칸이 벽으로 채워져 있음을 나타냅니다.
# 경주로의 출발점은 (0, 0) 칸(좌측 상단)이며, 도착점은 (N-1, N-1) 칸(우측 하단)입니다.
# 경주로는 상, 하, 좌, 우로 인접한 두 빈 칸을 연결하여 건설할 수 있으며,
# 벽이 있는 칸에는 경주로를 건설할 수 없습니다.

# 직선 도로 하나를 만들 때는 100원이 소요되며, 코너를 하나 만들 때는 500원이 추가로 듭니다.
# 경주로를 건설하는 데 필요한 최소 비용을 계산해야 합니다.

from collections import deque


def solution(board):
    n = len(board)
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    # 3차원 리스트 [x축][y축][방향]
    visited = [[[float('inf') for _ in range(4)] for _ in range(n)] for _ in range(n)]

    # d = 상하좌우 = 0,1,2,3
    # 0행0열 초기화
    for i in range(4):
        visited[0][0][i] = 0

    # 0행1열 초기화
    if board[0][1] != 1:
        queue.append([0, 1, 3, 100])  # x, y, d=우, cost=100원
        visited[0][1][3] = 100

    # 1행0열 초기화
    if board[1][0] != 1:
        queue.append([1, 0, 1, 100])  # x, y, d=하, cost=100원
        visited[1][0][1] = 100

    while queue:
        x, y, d, c = queue.popleft()  # x축, y축, 방향, 비용

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 상하 1, 좌우 -1
            # if i in (0, 1):
            #     nd = 1
            # elif i in (2, 3):
            #     nd = -1
            
            cost = c + 100
            # 온 방향 != 갈 방향
            # 온 방향으로 다시 돌아가는 경우는 비용이 더 커지므로 고려할 필요 없음.
            # '하'로 온 경우 직선도로인 '상'(다시 제자리)은 무시하고, 코너인 '좌', '우'만 고려하자.
            if d != i:
                cost += 500

            # 공간을 벗어날 경우 무시
            # if nx < 0 or nx >= n or ny < 0 or ny >= n:
            #     continue

            # 벽의 경우 무시
            # if board[nx][ny] == 1:
            #     continue

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] != 1:
                    # 작은 비용이 나타났을 경우 바꿔치기
                    if cost < visited[nx][ny][i]:
                        queue.append([nx, ny, i, cost])
                        visited[nx][ny][i] = cost

    # 가장 아래의 오른쪽에 최단 거리가 기록되있을 것이며, 반환
    return min(visited[n - 1][n - 1])


# print(solution(board=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
# print(solution(board=[[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
print(solution(
    board=[[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0]]))
