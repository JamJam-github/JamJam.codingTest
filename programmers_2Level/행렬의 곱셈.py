def solution(arr1, arr2):
    answer = []
    # print(len(arr1), len(arr2))
    n = len(arr1)
    m = len(arr2[0])
    l = len(arr2)

    for i in range(n):
        # print(i, arr1[i], end=' ')
        temp = []
        for j in range(m):
            # print((i, j))
            num = 0
            for k in range(l):
                # print(f'arr1[{i}][{k}] {arr1[i][k]} 기준으로 arr2[{k}][{j}] {arr2[k][j]} = {arr1[i][k] * arr2[k][j]}')
                num += arr1[i][k] * arr2[k][j]
            temp.append(num)
        answer.append(temp)

    return answer


# print(solution(arr1=[[1, 4], [3, 2], [4, 1]], arr2=[[3, 3], [3, 3]]))
# print(solution(arr1=[[2, 3, 2], [4, 2, 4], [3, 1, 4]], arr2=[[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
print(solution(arr1=[[2, 3, 2], [4, 2, 4], [3, 1, 4]], arr2=[[5, 4], [2, 4], [3, 1]]))


# 다른 사람의 풀이
# list(zip(*리스트)) : 2차원 리스트의 행과 열을 바꿔서 리턴
# 3행 2열 [[5, 4], [2, 4], [3, 1]] >> 2행 3열 [(5, 2, 3), (4, 4, 1)]

def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]


# print(productMatrix(A=[[2, 3, 2], [4, 2, 4], [3, 1, 4]], B=[[5, 4], [2, 4], [3, 1]]))