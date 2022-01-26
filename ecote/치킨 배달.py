# 치킨집을 M개 유지하면서 도시의 치킨 거리 합을 최소로 구하기.

# 치킨집을 기준으로 M개의 조합을 생성하고, 집 기준으로 해당 조합을 계산해보고
# 최종적으로 최소 조합의 결과를 리턴할 수 있다.

# (2 <= N <= 50), (1 <= M <= 13)
from itertools import combinations


def solution(n, m, array):
    house, chicken = [], []
    row = len(array)
    col = len(array[0])
    for i in range(row):
        for j in range(col):
            if array[i][j] == 1:
                house.append((i, j))
            elif array[i][j] == 2:
                chicken.append((i, j))

    candidates = list(combinations(chicken, m))
    print('chicken candi ::', candidates)

    def get_sum(candidate):
        result = 0
        for hx, hy in house:
            temp = float('inf')
            for cx, cy in candidate:
                temp = min(temp, abs(hx - cx) + abs(hy - cy))
            result += temp
        return result

    answer = float('inf')
    for candidate in candidates:
        answer = min(answer, get_sum(candidate))

    return answer


print(solution(n=5, m=3, array=[[0, 0, 1, 0, 0], [0, 0, 2, 0, 1], [0, 1, 2, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 2]]))
# print(solution(n=5, m=2, array=[[0, 2, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 0], [2, 0, 0, 1, 1], [2, 2, 0, 1, 2]]))
