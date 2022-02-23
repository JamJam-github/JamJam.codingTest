from collections import deque

board = [[0, 0, 0, 1, 1],
         [0, 0, 0, 1, 0],
         [0, 1, 0, 1, 1],
         [1, 1, 0, 0, 1],
         [0, 0, 0, 0, 0]]


def get_next_pos(pos, board):
    next_pos = []  # 현재 위치에서 이동할 수 있는 위치를 담을 변수
    pos = list(pos)
    x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx1 = x1 + dx[i]
        ny1 = y1 + dy[i]
        nx2 = x2 + dx[i]
        ny2 = y2 + dy[i]

        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            next_pos.append({(nx1, ny1), (nx2, ny2)})

    # 현재 로봇이 x축이 같으면 가로 -> 이제 세로로 회전하기
    if x1 == x2:
        # 아래, 위에 두 곳이 비어 있어야 회전 가능
        for i in [1, -1]:
            if board[x1 + i][y1] == 0 and board[x2 + i][y2] == 0:
                # 왼쪽, 오른쪽 회전
                next_pos.append({(nx1, ny1), (nx1 + i, ny1)})
                next_pos.append({(nx2, ny2), (nx2 + i, ny2)})
    # 현재 로봇이 y축이 같으면 세로 -> 이제 가로로 회전하기
    elif y1 == y2:
        for i in [1, -1]:
            if board[x1][y1 + i] == 0 and board[x2][y2 + i] == 0:
                # 위쪽, 아래쪽 회전
                next_pos.append({(nx1, ny1), (nx1, ny1 + i)})
                next_pos.append({(nx2, ny2), (nx2, ny2 + i)})

    return next_pos


def solution(board):
    n = len(board)
    # 맵 외곽에 벽을 두는 형태로 변형하기
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    # print(new_board)

    queue = deque()
    visited = []
    queue.append(({(1, 1), (1, 2)}, 0))
    visited.append({(1, 1), (1, 2)})

    while queue:
        pos, cost = queue.popleft()

        if (n, n) in pos:
            return cost

        # 이동 가능한 위치를 받아서 이동하기
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                queue.append((next_pos, cost + 1))
                visited.append(next_pos)

    return 0


print(solution(board))
