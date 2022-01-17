# BFS 너비 우선 탐색, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
# Queue 자료 구조를 사용한다.

# 동작 과정
# 1) 탐색 시작 노드를 큐에 삽입하고 방문 처리한다.
# 2) 큐에서 노드를 꺼낸 뒤 해당 노드의 인접한 노드 중에 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
# 3) 2번을 수행한다.
from collections import deque


graph = [
    [],
    [2, 3, 8],  # 1번 노드에 연결된 번호
    [1, 7],  # 2번 노드에 연결된 번호
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

def bfs(graph, start, visited):
    # 큐 구현을 위해
    queue = deque([start])

    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 원소를 꺼낸다
        v = queue.popleft()
        print(v, end=' ')

        # 꺼낸 원소에 인접한 노드를 큐에 넣고 방문처리
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


print(bfs(graph, 1, visited))