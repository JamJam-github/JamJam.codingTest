# 다익스트라 알고리즘, 우선순위 큐 적용 (heapq 최소힙)
# 배달

from collections import defaultdict
import heapq


def solution(N, road, K):
    # 최단 거리 테이블을 모두 무한으로 초기화
    dist = {i: float('inf') if i != 1 else 0 for i in range(1, N + 1)}

    nRoad = defaultdict(list)
    for v in road:
        nRoad[v[0]].append((v[1], v[2]))
        nRoad[v[1]].append((v[0], v[2]))

    queue = []
    heapq.heappush(queue, (0, 1))  # (거리, 노드)로 구성되어야 '거리'값이 우선순위 값이 된다.

    while queue:
        cur_dist, cur_town = heapq.heappop(queue)

        if dist[cur_town] < cur_dist:
            continue

        # 연결된 방문할 노드
        for nxt_town, d in nRoad[cur_town]:
            # 현재 가중치 + 거리 < 방문노드의 가중치
            # 초과될 경우 pass, 더 이상 아래 노드도 진행하지 않음
            if cur_dist + d < dist[nxt_town]:
                dist[nxt_town] = cur_dist + d
                heapq.heappush(queue, [cur_dist + d, nxt_town])

    print('total dist', dist)
    return len([True for i in dist.values() if i <= K])


print(solution(N=5,
               road=[[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]],
               K=3))
# print(solution(N=6,
#                road=[[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]],
#                K=4))
