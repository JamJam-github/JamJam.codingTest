# [1차] 프렌즈4블록

# 1) 전체 탐색으로 프렌즈블록이 터질 곳의 좌표를 찾는다.
# 2) 해당 좌표는 set 으로 받아서 중복으로 터질 곳은 제외한다. (마지막 배열에서 지워진 총 개수를 세어도 된다.)
# 3) 블록이 터진 부분은 '0'으로 바꿔주기
# 4) '0'으로 지워진 부분에 위에 있는 블록들을 아래로 채워준다. (열 단위로 아래로만 움직이는 개념)
# 5) 1~4번을 반복해서 터질 곳의 좌표를 찾지 못한다면 break

# list(zip(*리스트)) : 2차원 리스트의 행과 열을 바꿔서 리턴


def solution(m, n, board):
    answer = 0
    print('board 블록 초기 상태::')
    for i in range(m):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

    def del_block(board):
        blockSet = set()
        for i in range(m - 1):
            for j in range(n - 1):
                block = board[i][j]
                if block == '0':
                    pass
                elif block == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                    blockSet.add((i, j))
                    blockSet.add((i, j + 1))
                    blockSet.add((i + 1, j))
                    blockSet.add((i + 1, j + 1))

        return blockSet

    while True:
        block = del_block(board)
        print('set ::', block, '터진 블록 수 ::', len(block))

        if block:
            answer += len(block)
            board = list(map(list, board))

            for x, y in block:
                board[x][y] = '0'

            print('board 블록 맞춘 후 ::')
            for i in range(m):
                for j in range(n):
                    print(board[i][j], end=' ')
                print()

            board = list(zip(*board))
            # print('board 열(=col) 순서대로 가져오기::', board)
            for i, v in enumerate(board):
                board[i] = '0' * v.count('0') + ''.join(v).replace('0', '')
            board = list(zip(*board))
            print('board 행(=row) 순서대로 가져오기::')
            for i in range(m):
                for j in range(n):
                    print(board[i][j], end=' ')
                print()

        else:
            return answer

    return answer


# print(solution(m=6, n=6, board=["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(solution(m=4, n=4, board=["ABCD", "BACE", "BCDD", "BCDD"]))
