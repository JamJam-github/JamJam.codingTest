# 잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태이고
# 특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.

# 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다.
# 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만,
# 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며
# 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다.


def solution(key, lock):
    M, N = len(key), len(lock)

    # 중심에 자물쇠를 놓을 큰 보드를 생성하여
    # 키를 가지고 한칸씩 이동해보면서 열리는지 확인하기 위함.
    board = [[0] * (M * 2 + N) for _ in range(M * 2 + N)]
    print(board)

    def attach(x, y, M, key, board):
        # key 크기만큼 board에 넣어보기
        for i in range(M):
            for j in range(M):
                board[x + i][y + j] += key[i][j]

    def detach(x, y, M, key, board):
        # key 크기만큼 board에서 빼주기
        for i in range(M):
            for j in range(M):
                board[x + i][y + j] -= key[i][j]

    def rotate(arr):
        # n = len(arr)
        # ret = [[0] * n for _ in range(n)]
        #
        # for i in range(n):
        #     for j in range(n):
        #         ret[j][n - 1 - i] = arr[i][j]
        # return ret
        return list(zip(*arr[::-1]))  # 열->행을 행->열로 바꾸기

    def check(board, M, N):
        for i in range(N):
            for j in range(N):
                if board[M + i][M + j] != 1:
                    return False
        return True

    # 자물쇠 중앙 배치
    for i in range(N):
        for j in range(N):
            board[M + i][M + j] = lock[i][j]

    rotated_key = key
    for i in range(4):
        rotated_key = rotate(rotated_key)
        for x in range(1, M + N):
            for y in range(1, M + N):
                attach(x, y, M, rotated_key, board)

                if check(board, M, N):
                    return True

                detach(x, y, M, rotated_key, board)

    return False


print(solution(key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]],
               lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
