# 가장 큰 정사각형 찾기

# 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return

def solution(board):
    m = len(board)
    n = len(board[0])

    for i in range(1, m):
        for j in range(1, n):
            if board[i][j]:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1

    answer = 0
    for i in range(m):
        temp = max(board[i])
        answer = max(answer, temp)

    return answer ** 2

print(solution(board=[[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
print(solution(board=[[0, 0, 1, 1], [1, 1, 1, 1]]))
print(solution(board=[[1]]))
