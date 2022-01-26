# 시뮬레이션
# 사과를 먹으면 뱀의 길이가 늘어난다.
# 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝난다.
# 처음 뱀의 길이는 1이며, 오른쪽을 향한다.

# 규칙
# 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킨다.
# 이동한 칸에 사과가 있으면, 사과는 없어지고 꼬리는 움직이지 않는다.
# 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이 변화 없음
# 이 게임이 몇 초에 끝나는지 계산하세요.

# 향하고 있는 방향만 바꿔주면 된다.
def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def solution(n, k, apples, l, d_arr):
    # 보드의 크기 n, 사과의 개수 k, 사과의 위치 apples
    # 뱀의 방향 변환 횟수 L, 변환 정보 d_arr [X, C] 형태

    # 현재 방향
    direction = 0
    # 동남서북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    board = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # 사과를 표시한 맵
    for i, j in apples:
        board[i][j] = 1

    x, y = 1, 1  # 뱀의 머리 위치
    board[x][y] = 2  # 뱀이 존재하는 위치 표시
    body = [(x, y)]  # 꼬리 포함 정보
    time = 0
    l_index = 0

    while True:
        time += 1

        # 방향으로 이동 후 범위를 벗어나면 종료
        nx = x + dx[direction]
        ny = y + dy[direction]
        if not 1 <= nx <= n or not 1 <= ny <= n or board[nx][ny] == 2:
            break

        # 매 시점마다 뱀의 위치를 기록
        # 사과를 만나면 머리는 이동하고, 꼬리는 그대로
        if board[nx][ny] == 1:
            board[nx][ny] = 2
            body.append((nx, ny))
        # 사과가 없으면 머리는 이동하고, 꼬리칸을 비운다.
        else:
            board[nx][ny] = 2
            body.append((nx, ny))

            px, py = body.pop(0)
            board[px][py] = 0

        x, y = nx, ny
        # 뱀의 방향 변환
        if l_index < l and d_arr[l_index][0] == time:
            direction = turn(direction, d_arr[l_index][1])
            l_index += 1

    return time


print(solution(n=6, k=3, apples=[[3, 4], [2, 5], [5, 3]], l=3, d_arr=[[3, 'D'], [15, 'L'], [17, 'D']]))
