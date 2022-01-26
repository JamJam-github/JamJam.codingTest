# 다익스트라 알고리즘
# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시 번호 X
# X로부터 출발하여 도달할 수 있는 도시 중에서 최단 거리가 K인 모든 도시를 출력

import heapq
from collections import defaultdict


def solution(n, m, k, x, array):
    # X 지점을 기준으로 각 지점의 최단거리
    dist = {i: float('inf') if i != x else 0 for i in range(1, n + 1)}
    # print(dist)

    graph = defaultdict(list)
    for i in array:
        graph[i[0]].append(i[1])

    queue = []
    heapq.heappush(queue, (0, 1))  # (거리, 노드)로 구성되어야 '거리'값이 우선순위 값이 된다.

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)

        if dist[cur_node] < cur_dist:
            continue

        # 연결된 방문할 노드
        for nxt_town in graph[cur_node]:
            # 현재 가중치 + 거리 < 방문노드의 가중치
            # 초과될 경우 pass, 더 이상 아래 노드도 진행하지 않음
            if cur_dist + 1 < dist[nxt_town]:
                dist[nxt_town] = cur_dist + 1
                heapq.heappush(queue, [cur_dist + 1, nxt_town])

    # print('total dist', dist)
    answer = [i for i, v in dist.items() if v == k]
    return answer if answer else -1


print(solution(n=4, m=4, k=2, x=1, array=[[1, 2], [1, 3], [2, 3], [2, 4]]))
print(solution(n=4, m=3, k=2, x=1, array=[[1, 2], [1, 3], [1, 4]]))
print(solution(n=4, m=4, k=1, x=1, array=[[1, 2], [1, 3], [2, 3], [2, 4]]))
