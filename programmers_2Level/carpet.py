# 카펫

def solution(brown, yellow):
    answer = []
    n = brown + yellow
    divisor = [i for i in range(3, (n // 2)) if n % i == 0]
    # print(divisor)

    for i in range(len(divisor)):
        x = (n // divisor[i]) - 2
        y = divisor[i] - 2
        # print(n, divisor[i], x, y)
        if (x * y) == yellow:
            return [n // divisor[i], divisor[i]]

    return answer


print(solution(brown=10, yellow=2))
# print(solution(brown=8, yellow=1))
# print(solution(brown=24, yellow=24))


# 다른 사람의 풀이
# 둘레의 길이를 이용해

def solution_other(brown, yellow):
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            if 2 * (i + yellow // i) == brown - 4:
                return [yellow // i + 2, i + 2]
