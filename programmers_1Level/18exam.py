# [1차] 비밀지도

arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
n = 6


def solution(n, arr1, arr2):
    array1 = [format(i, 'b').zfill(n) for i in arr1]
    array2 = [format(i, 'b').zfill(n) for i in arr2]
    answer = []
    for i, v in enumerate(array1):
        tmp = ''
        for j, val in enumerate(v):
            tmp += '#' if int(val) or int(array2[i][j]) else ' '
        answer.append(tmp)

    return answer


print(solution(n, arr1, arr2))


# 다른 사람의 풀이
# zip 함수 !! 동일한 개수로 이루어진 그룹의 데이터를 서로 엮어준다.
# bin 함수 !! integer를 이진수(binary) 문자열로 돌려준다.
answer = []
for i, j in zip(arr1, arr2):
    a12 = bin(i | j)[2:].rjust(n, '0')
    a12 = a12.replace('1', '#')
    a12 = a12.replace('0', ' ')
    answer.append(a12)

print(answer)