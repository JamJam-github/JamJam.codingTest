# 쿼드압축 후 개수 세기

# 0과 1로 이루어진 2n x 2n 크기의 2차원 정수 배열 arr이 있습니다.
# 이 arr을 쿼드 트리와 같은 방식으로 압축하고자 합니다.
# 리스트를 자르지 않고 인덱스를 계산해서 크기 만큼 반복문으로 확인한다.

def solution(arr):
    answer = [0, 0]
    n = len(arr)

    def quad(x, y, n):
        temp = arr[x][y]
        print(f'temp={temp}, quad({x}, {y}, {n})')
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != temp:
                    print(f'{n}크기로 압축 실패')
                    quad(x, y, n // 2)
                    quad(x, y + n // 2, n // 2)
                    quad(x + n // 2, y, n // 2)
                    quad(x + n // 2, y + n // 2, n // 2)
                    return
        answer[temp] += 1
        print(f'answer[{temp}] + 1 추가')

    quad(0, 0, n)
    return answer


print(solution(arr=[[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
# print(solution(
#     arr=[[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
#          [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]))
