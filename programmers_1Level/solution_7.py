# 행렬의 덧셈

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer2 = []
        for j in range(len(arr1[i])):
            answer2.append(arr1[i][j] + arr2[i][j])
        answer.append(answer2)

    return answer


arr1 = [[1, 2, 3], [2, 3, 4]]
arr2 = [[3, 4, 5], [5, 6, 7]]

print(solution(arr1, arr2))
print()

# 다른 사람의 풀이
# 1) numpy 라이브러리를 사용하여 numpy.array(배열)로 numpy 배열을 생성한다.
#    numpy 배열은 각 요소를 사칙연산 가능하다.
# import numpy as np
# arr1 = np.array(arr1)
# arr2 = np.array(arr2)
# answer = arr1 + arr2

# 2) zip 함수 사용하기
# 동일한 개수로 이루어진 그룹의 데이터를 서로 엮어준다.
# answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
