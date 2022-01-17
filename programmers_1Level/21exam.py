# 최소직사각형

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]


def min_rectangle(sizes):
    t = list(map(lambda x: [x[1], x[0]] if x[0] > x[1] else [x[0], x[1]], sizes))
    xMax = max(t, key=lambda x: x[0])[0]
    yMax = max(t, key=lambda x: x[1])[1]
    return xMax * yMax


min_rectangle(sizes)


# 다른 사람의 풀이
# 리스트 행 전체 기준으로 max 값을 단일로 출력할 수 있음.

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
