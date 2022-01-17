# 행렬 테두리 회전하기
# rows x columns 크기인 행렬
# x1 행 y1 열부터 x2 행 y2 열까지의 영역에 해당하는 직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전합니다.
# 회전들의 목록 queries가 주어질 때, 각 회전들을 배열에 적용한 뒤,
# 그 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return


# 2차원 배열에서 가로, 세로를 진행하는 반복문 방향과
# 데이터를 끌어오는 방향을 반대로 진행해서 변경해준다.
# 진행 완료 후 1개의 데이터가 손실되는데, 처음 시작 데이터를 temp1에 놓고 마지막 손실 데이터 자리에 넣기

def solution(rows, columns, queries):
    answer = []
    arr = [[row * columns + col + 1 for col in range(columns)] for row in range(rows)]

    for a, b, c, d in queries:
        x1, y1, x2, y2 = a - 1, b - 1, c - 1, d - 1
        temp1 = arr[x1][y1]
        minNum = temp1
        # print(f'({(x1, y1)} ~ {(x2, y2)}) 회전할게, 임시::{temp1}')

        for t in range(x1, x2):
            # print(f'왼쪽 세로 ({t}, {y1}) {arr[t][y1]}에 ({t + 1}, {y1}) {arr[t + 1][y1]}를 넣고')
            temp2 = arr[t + 1][y1]
            arr[t][y1] = temp2
            minNum = min(minNum, temp2)

        for z in range(y1, y2):
            # print(f'밑 가로 ({x2}, {z}) {arr[x2][z]}에 ({x2}, {z + 1}) {arr[x2][z + 1]}를 넣고')
            temp2 = arr[x2][z + 1]
            arr[x2][z] = temp2
            minNum = min(minNum, temp2)

        for y in range(x2, x1, -1):
            # print(f'오른쪽 세로 ({y}, {y2}) {arr[y][y2]}에 ({y - 1}, {y2}) {arr[y - 1][y2]}를 넣고')
            temp2 = arr[y - 1][y2]
            arr[y][y2] = temp2
            minNum = min(minNum, temp2)

        for x in range(y2, y1, -1):
            # print(f'가로 ({x1}, {x}) {arr[x1][x]}에 ({x1}, {x - 1}) {arr[x1][x - 1]}를 넣고')
            temp2 = arr[x1][x - 1]
            arr[x1][x] = temp2
            minNum = min(minNum, temp2)

        arr[x1][y1 + 1] = temp1
        answer.append(minNum)

        # print(arr)

    return answer


print(solution(rows=6, columns=6, queries=[[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
