# 시뮬레이션
# N * M 크기의 직사각형 맵 생성
# 각각의 칸은 0: 육지, 1: 바다
# (x, y)에 [0: 북쪽, 1: 동쪽,  2: 남쪽, 3: 서쪽]을 바라보고 서 있는 캐릭터

# 1. 현재 위치에서 왼쪽(반시계 방향)으로 갈 곳을 정한다.
# 2. 왼쪽으로 가보지 않은 칸이 존재하면 왼쪽으로 회전하고 전진한다.
#    2-1. 가보지 않은 칸이 없으면 1단계로 돌아간다.
# 3. 네 방향 모두 가본 칸이거나 바다인 경우
#    3-1. 바라보는 방향을 유지한 채로 뒤로가고 1단계로 돌아간다.
#    3-2. 뒤쪽 방향이 바다인 경우 움직임을 멈춘다. (종료시점)
# 4. 최종적으로 방문한 칸의 수를 출력한다.


# 왼쪽 회전, 현재 방향에서 반시계 방향으로 변화
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


def solution(n, m, x, y, d, maps):
    answer = 1
    global direction

    # 북 동 남 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    turn_cnt = 0
    direction = d
    visited = [[0 for _ in range(m)] for _ in range(n)]

    # 초기 방문표시
    visited[x][y] = 1

    # 계속 회전+이동하고 중단 시점 설정
    while True:
        # 1
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 2
        if visited[nx][ny] == 0 and maps[nx][ny] == 0:
            x, y = nx, ny
            visited[nx][ny] = 1
            turn_cnt = 0
            answer += 1
            continue
        # 2-1
        turn_cnt += 1

        # 3
        if turn_cnt == 4:
            # 3-1
            x -= dx[direction]
            y -= dy[direction]
            turn_cnt = 0
            # 3-2
            if maps[x][y] == 1:
                break

    return answer


print(solution(n=4, m=4, x=1, y=1, d=0,
               maps=[[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]))
