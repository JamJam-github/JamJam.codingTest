# (03) 이진탐색

L = [2, 3, 5, 6, 9, 11, 15]
x = 6


def solution(L, x):
    answer = -1
    lower, upper, mid = 0, len(L) - 1, 0

    if L[upper] < x:
        return answer

    while lower <= upper:
        mid = (lower + upper) // 2
        if L[mid] == x:
            answer = mid
            break
        elif L[mid] < x:
            lower = mid + 1
        else:
            upper = mid - 1

    return answer


print(solution(L, x))
