# 플로이드 워셜
# 공중 미래 도시에는 1번부터 N번까지의 회사가 있는데
# 특정 회사끼리는 서로 도로를 통해 연결되어 있다.
# 연결된 2개의 회사는 양방향으로 이동할 수 있다.
# 서로 연결되어 있다면, 1만큼의 시간으로 이동할 수 있다.

# A는 1번 회사에서 출발하여
# K번 회사에 방문한 뒤 X번 회사로 가는 것이 목표이다.

def solution(n, m, array, x, k):
    graph = [[int(1e9)] * (n + 1) for _ in range(n + 1)]

    # 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    # 간선의 정보를 입력받고, 모든 거리비용은 1로 동일하다.
    for i in range(m):
        a, b = array[i]
        graph[a][b] = 1
        graph[b][a] = 1
    # print('graph::', graph)

    # 1 -> K -> X까지의 최단거리
    # 최종적으로 1번노드에서 X노드까지를 출력
    
    # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    dist = graph[1][k] + graph[k][x]

    return -1 if dist >= int(1e9) else dist


# 회사의 개수 n과 경로의 개수 m (1 <= n, m <= 100)
print(solution(n=5, m=7, array=[[1, 2], [1, 3], [1, 4], [2, 4], [3, 4], [3, 5], [4, 5], [4, 5]],
               x=4, k=5))
