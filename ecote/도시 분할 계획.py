# 크루스칼 알고리즘(최소 신장 트리 알고리즘)
# 마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다.
# 길은 어느 방향으로든지 다닐 수 있고, 길을 유지하는데 드는 유지비가 있다.
# 마을을 2개로 분할할 계획을 세우고 있다.
# 마을을 분리할 때, 각 분리된 마을이 서로 연결되도록 분할해야 한다.
# 마을에는 집이 하나 이상 있어야 한다.

# 두 집 사이에 경로가 항상 존재하면 길을 더 없애고 유지비의 합을 최소로 리턴
# M줄에 걸쳐 길의 정보가 A, B, C로 주어지고, A와 B를 연결하는 유지비가 C

# 루트 노드를 찾을 때까지 재귀적으로 호출
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def solution(n, m, array):
    # 2개의 최소 신장 트리를 만들기 위해서
    # 1개의 최소 신장 트리를 구성하고 가장 비용이 큰 간선을 제거하는 것이다.
    # 1. (유지비, 집번호) 형태로 유지비 순서로 정렬한다.
    # 2. 사이클이 발생하지 않는 경우만 최소 비용으로 포함한다.
    parent = [i for i in range(n + 1)]
    trees = [(array[i][2], array[i][0], array[i][1]) for i in range(m)]
    trees.sort()
    # print(trees)
    result = last = 0

    for i in range(m):
        cost, a, b = trees[i]
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a == b:
            continue

        if a < b:
            parent[a] = b
        elif a > b:
            parent[b] = a
        result += cost
        last = cost

    return result - last


print(solution(n=7, m=12, array=[[1, 2, 3],
                                 [1, 3, 2],
                                 [3, 2, 1],
                                 [2, 5, 2],
                                 [3, 4, 4],
                                 [7, 3, 6],
                                 [5, 1, 5],
                                 [1, 6, 2],
                                 [6, 4, 1],
                                 [6, 5, 3],
                                 [4, 5, 3],
                                 [6, 7, 4]]))
