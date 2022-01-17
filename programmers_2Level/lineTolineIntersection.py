# 교점에 별 만들기

# 두 직선의 교점이 유일하게 존재할 경우 교점 공식
# Ax + By + E = 0
# Cx + Dy + F = 0
# x = (BF - ED) / (AD - BC)
# y = (EC - AF) / (AD - BC)
# 단, (AD - BC) = 0 이 되는 경우 두 직선은 평행(=일치)이 되어 교점이 없음.

# 모든 교점을 구한 후, 모든 교점이 포함되는 최소 삼각형 모양을 그릴 수 있도록
# [가로 x 세로] 길이를 구해서 출력하기

def solution(line):
    answer = []
    inter = set()
    xmax, ymax, xmin, ymin = -float('inf'), -float('inf'), float('inf'), float('inf')

    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            A, B, E = line[i]
            C, D, F = line[j]

            mod = A * D - B * C
            if mod:
                # 나머지가 0인 경우 정수
                if (B * F - D * E) % mod or (C * E - A * F) % mod:
                    continue

                x = int((B * F - D * E) / mod)
                y = int((C * E - A * F) / mod)
                inter.add((x, y))
                xmax, ymax = max(xmax, x), max(ymax, y)
                xmin, ymin = min(xmin, x), min(ymin, y)
                # print(line[i], line[j], '교점 존재', (x, y))
            else:
                # print(line[i], line[j], '평행 또는 일치')
                continue
    # print(inter)
    # print('max:', xmax, ymax, 'min:', xmin, ymin)
    for i in range(ymax, ymin - 1, -1):
        temp = ""
        for j in range(xmin, xmax + 1):
            if (j, i) in inter:
                # print((i, j), '존재')
                temp += "*"
            else:
                temp += "."
        answer.append(temp)
    return answer


print(solution(line=[[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print('-----------------------')
print(solution(line=[[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
