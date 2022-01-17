import heapq
from collections import defaultdict


# 다익스트라 알고리즘

def solution(n, s, a, b, fares):
    answer = float('inf')

    def dijkstra(s, e):  # s부터 e까지 가는 시간 구하기
        dist = [float('inf')] * (n + 1)
        dist[s] = 0

        queue = [[0, s]]  # [cost, node]
        heapq.heapify(queue)

        while queue:
            cur_cost, cur_node = heapq.heappop(queue)

            # 해당노드를 방문하는데 드는 비용이 기존 최소비용보다 큰 경우는 무시
            if cur_cost > dist[cur_node]:
                continue

            # 방문할 노드
            for nxt_node, new_cost in graph[cur_node]:
                # 현재 가중치 + 거리 < 방문노드의 가중치
                # 초과될 경우 pass, 더 이상 아래 노드도 진행하지 않음
                if cur_cost + new_cost < dist[nxt_node]:
                    dist[nxt_node] = cur_cost + new_cost
                    heapq.heappush(queue, [cur_cost + new_cost, nxt_node])

        return dist[e]

    graph = defaultdict(list)
    for i, j, cost in fares:
        graph[i].append([j, cost])
        graph[j].append([i, cost])
    print(graph)

    for i in range(1, n + 1):
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

    return answer


print(solution(n=6, s=4, a=6, b=2,
               fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                      [1, 6, 25]]))
