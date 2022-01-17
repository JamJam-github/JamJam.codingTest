# 배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다.
# 이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다.
# 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다.

def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    return sum(a * b for a, b in zip(A, B))


print(solution(A=[1, 4, 2], B=[5, 4, 4]))
print(solution(A=[1, 2], B=[3, 4]))
