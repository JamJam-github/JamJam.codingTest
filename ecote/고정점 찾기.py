# 리스트 내 인덱스와 값이 동일한 원소를 찾기
# # O(logN)으로 설계


def solution(n, data):
    answer = -1
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        # print(f'left = {left}, right = {right}, mid = {mid}')
        if mid < data[mid]:
            right = mid - 1
        elif mid > data[mid]:
            left = mid + 1
        else:
            answer = mid
            break
    return answer


print(solution(n=5, data=[-15, -6, 1, 3, 7]))
print(solution(n=7, data=[-15, -4, 2, 8, 9, 13, 15]))
print(solution(n=7, data=[-15, -4, 3, 8, 9, 13, 15]))
