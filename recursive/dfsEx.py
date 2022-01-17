# DFS 깊이 우선 탐색, 깊은 부분을 우선적으로 탐색하는 알고리즘
# stack 자료 구조를 이용한다.

# 동작 과정
# 1) 탐색 노드를 스택에 넣고 방문처리
# 2) 최상단 원소를 기준으로 인접한 노드가 있으면 인접노드로 방문한다.
# 3) 2번을 수행한다. (만약, 인접한 노드가 없는 경우 해당 원소를 스택에서 pop 하고 2번을 수행)

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
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


def dfs(graph, v, visited):
    # 방문 처리
    visited[v] = True
    # 탐색 순서를 출력
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# v= 시작점 1번 부터 방문을 시작하겠다.
print(dfs(graph, 1, visited))
