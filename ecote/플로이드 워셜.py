# 플로이드 워셜 알고리즘
# 한 지점에서 특정 지점의 최단 거리
# (한 지점에서 특정 지점의 최단 거리) * N번 = 모든 지점에서 모든 지점으로 가는 최단 거리

def solution(n, m, nodes):
    graph = [[int(1e9)] * (n + 1) for _ in range(n + 1)]

    # 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    # 간선의 정보를 입력받아 그 값으로 초기화
    for i in range(m):
        a, b, c = nodes[i]
        graph[a][b] = c

    # 점화식에 따라 플로이드 워셜 알고리즘을 수행    
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == int(1e9):
                print('INF', end=' ')
            else:
                print(graph[a][b], end=' ')
        print()

    return ''


print(solution(n=4, m=7, nodes=[[1, 2, 4], [1, 4, 6], [2, 1, 3], [2, 3, 7], [3, 1, 5], [3, 4, 4], [4, 3, 2]]))
