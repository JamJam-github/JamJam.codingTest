# 개구리가 0번 위치에서 X번 위치로 이동할때 걸리는 시간
# A[K] 배열은 K초당 나뭇잎이 위치하는 곳

# A[0] = 1, A[1] = 3 일때
# 0초에 1번 나뭇잎이 위치하고, 1초에 3번 나뭇잎이 위치한다.
# 최종적으로 X번 위치까지 모두 나뭇잎이 채워져있는 경우 최종적인 시간을 리턴한다.

def solution(X, A):
    # 배열 1에서 X 위치까지 채울 나뭇잎 배열 
    arr = [-1 for i in range(X + 1)]
    for i in range(len(A)):
        # 빠른 시간만 저장해야 하므로 최초시에 저장
        if arr[A[i]] == -1:
            arr[A[i]] = i

    # print(arr)
    answer = 0
    for i in range(1, X + 1):
        # 비어있는 나뭇잎이 있으면 실패
        if arr[i] == -1:
            answer = -1
            break
        else:
            answer = max(answer, arr[i])

    return answer


print(solution(X=5, A=[1, 3, 1, 4, 2, 3, 5, 4]))
