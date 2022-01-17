# s에서 각 지점을 가는 가중치를 구하고
# 각 지점에서 a와 b를 가는 가중치를 구한다.
# 각 지점 + a + b 합산의 min 값이 answer
import heapq
from collections import defaultdict


# 다익스트라 알고리즘
def dijkstra(dist, graph, start):
    queue = []
    heapq.heappush(queue, [start, 0])  # 항상 s번 마을에서 시작, 초기 cost = 0
    while queue:
        cur_town, cur_dist = heapq.heappop(queue)

        for nxt_town, d in graph[cur_town]:
            if nxt_town != start and cur_dist + d < dist[nxt_town]:
                dist[nxt_town] = cur_dist + d
                heapq.heappush(queue, [nxt_town, cur_dist + d])


def solution(n, s, a, b, fares):
    answer = float('inf')
    graph = defaultdict(list)
    for i in fares:
        graph[i[0]].append((i[1], i[2]))
        graph[i[1]].append((i[0], i[2]))

    # S지점을 기준으로 각 지점의 최소거리
    dist = {i: float('inf') if i != s else 0 for i in range(1, n + 1)}
    dijkstra(dist, graph, s)

    # A지점을 기준으로 각 지점의 최소거리
    dist2 = {i: float('inf') if i != a else 0 for i in range(1, n + 1)}
    dijkstra(dist2, graph, a)

    # B지점을 기준으로 각 지점의 최소거리
    dist3 = {i: float('inf') if i != b else 0 for i in range(1, n + 1)}
    dijkstra(dist3, graph, b)

    for i in range(1, n + 1):
        total = dist[i] + dist2[i] + dist3[i]
        answer = min(answer, total)

    return answer


print(solution(n=6, s=4, a=6, b=2,
               fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(n=7, s=3, a=4, b=1,
               fares=[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
