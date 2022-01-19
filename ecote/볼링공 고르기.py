#

def solution(n, m, data):
    # A가 무게가 k인 공을 선택할 때의 경우의 수 = (무게가 k인 공의 개수) * (B가 선택하는 경우의 수)
    array = [0] * 11
    for i in data:
        array[i] += 1

    result = 0
    for i in range(1, m + 1):
        n -= array[i]
        result += array[i] * n
    return result


print(solution(n=5, m=3, data=[1, 3, 2, 3, 2]))
print(solution(n=8, m=5, data=[1, 5, 4, 3, 2, 4, 5, 2]))
