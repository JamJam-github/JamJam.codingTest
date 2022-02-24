# 1부터 연속된 숫자 중 누락된 정수를 반환하기
# N은 [ 1 .. 100,000 ] 범위 내의 정수
# 배열 A의 각 요소는 [ −1,000,000 .. 1,000,000 ] 범위 내의 정수

from bisect import bisect_left


def solution(A):
    arr = list(set(A))
    arr.sort()
    pos = bisect_left(arr, 1)
    arr = arr[pos:]
    # print(arr)

    answer = 1
    if arr:
        new_arr = [i for i in range(1, len(arr) + 1)]
        diff = list(set(new_arr) - set(arr))
        # print(new_arr, diff)
        if diff:
            answer = min(diff)
        else:
            answer = len(arr) + 1

    return answer


# 초 간단....
# 배열은 N 크기 100,000 으로 반복문 가능하니까
def solution_other(A):
    A.sort()
    min = 1
    for i in A:
        if i == min:
            min += 1
    return min


print(solution(A=[-1000000, 1000000]))
