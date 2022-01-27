# 3개의 장애물을 설치해서 모든 학생들이 감시를 피할 수 있는지 여부를 리턴
# 'X'는 빈칸, 'S'는 학생, 'T'는 선생님
# DFS 이용하지 않고 조합으로 풀이

from itertools import combinations


def watch(n, board, x, y, d):
    # 왼쪽, 오른쪽, 상, 하
    if d == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1

    if d == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1

    if d == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1

    if d == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1

    return False


def process(n, board, teachers):
    for x, y in teachers:
        for i in range(4):
            if watch(n, board, x, y, i):
                return True
    return False


def solution(n, board):
    # 1) 3개의 빈 공간의 조합을 생성
    # 2) 해당 빈 공간에 장애물로 표시하기
    # 3)  선생님의 감시를 피할 수 있는지 체크
    #   3-1) 선생님은 상하좌우 확인하고 비어있다면 해당 방향으로 직진 (watch)
    #        학생 발견시 true 리턴, 학생 미발견시 false 리턴 후 'YES' 결과
    # 4) true 리턴된 경우(=피할 수 없음) 시도한 장애물 삭제 후 반복
    result = ''
    teachers, spaces = [], []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'T':
                teachers.append((i, j))
            elif board[i][j] == 'X':
                spaces.append((i, j))

    # 1) 
    for data in combinations(spaces, 3):
        # 2)
        for x, y in data:
            board[x][y] = 'O'

        # 3)
        if not process(n, board, teachers):
            result = True
            break

        # 4)
        for x, y in data:
            board[x][y] = 'X'

    return 'YES' if result else 'NO'


print(solution(n=5, board=[['X', 'S', 'X', 'X', 'T'],
                           ['T', 'X', 'S', 'X', 'X'],
                           ['X', 'X', 'X', 'X', 'X'],
                           ['X', 'T', 'X', 'X', 'X'],
                           ['X', 'X', 'T', 'X', 'X']]))

print(solution(n=4, board=[['S', 'S', 'S', 'T'],
                           ['X', 'X', 'X', 'X'],
                           ['X', 'X', 'X', 'X'],
                           ['T', 'T', 'T', 'X']]))
