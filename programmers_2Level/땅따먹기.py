# 땅따먹기

def solution(land):
    # 탐욕법
    # land에 이전행의 최댓값을 더해가면서, 가능한 경우중에서 좋은 경우만을 남기도록 탐욕적 기법을 사용
    # 단, 이전행에서 같은 열(j)은 제외

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i - 1][: j] + land[i - 1][j + 1:]) + land[i][j]
    return max(land[-1])


print(solution(land=[[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
