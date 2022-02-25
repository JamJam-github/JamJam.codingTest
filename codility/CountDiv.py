# [A..B] 범위 내에서 K로 나눌 수 있는 정수의 개수를 반환합니다.
# [6..11] 범위 내에서 2로 나눌 수 있는 3개의 숫자, 즉 6, 8 및 10이 있기 때문입니다.
# A 및 B는 [ 0 .. 2,000,000,000 ] 범위 내의 정수입니다 .
# K는 [ 1 .. 2,000,000,000 ] 범위 내의 정수입니다 .

# 값이 크다. 반복문 사용하지 않기

def solution(A, B, K):
    AK = divmod(A, K)
    BK = divmod(B, K)
    if AK[1] == 0:
        answer = BK[0] - AK[0] + 1
    else:
        answer = BK[0] - AK[0]

    return answer


print(solution(A=6, B=11, K=2))