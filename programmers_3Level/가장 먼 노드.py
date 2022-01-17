# n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다.
# 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다.

# answer = [0, 1, 1, 2, 2, 2] max(answer)과 같은 것을 뽑아서 return len

from collections import defaultdict
from collections import deque


def solution(n, vertex):
    answer = [0] * (n + 1)
    visited = [False] * (n + 1)

    graph = defaultdict(list)
    for i, j in vertex:
        graph[i].append(j)
        graph[j].append(i)
    print(graph)

    # 모든 정점의 최소 거리를 계산해야 하는데 DFS로 풀게 되면 깊이 우선으로 값이 다르게 도출된다.
    # 최소값으로 저장하면 되겠지만 시간 초과를 만나게 될 것
    # BFS는 인접한 정점을 순서대로 탐색하여 가까운 순으로 자동 거리 매김이 된다. (최소값 정의가 필요없음)
    # 거리 배열에 갱신되는 값은 자동적으로 항상 최소값을 가지게 된다.

    queue = deque()
    visited[1] = True
    queue.append(1)

    while queue:
        value = queue.popleft()

        for node in graph[value]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)
                # if not answer[node]:
                #     answer[node] = count

                # 기존 정점이 가지고 있는 거리에 1을 더해 값을 갱신한다.
                # dist[인접한 정점] = dist[큐에서 꺼내온 기존 데이터] + 1
                answer[node] = answer[value] + 1
    return len([i for i in answer if max(answer) == i])


print(solution(n=6, vertex=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
