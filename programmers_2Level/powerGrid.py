# 전력망을 둘로 나누기

# n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있습니다.
# 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다.
# 가능한 비슷하도록 두 전력망으로 나누었을 때, 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return

# wires(전선 정보)를 차례대로 끊어가면서 한쪽의 전력망을 계산하면 count 개
# 다른 한쪽의 전력망은 (송전탑 총 개수 n - count)개
# 전선 정보를 나타내는 그래프를 만들기.

from collections import defaultdict


def solution(n, wires):
    answer = []
    global count

    graph = defaultdict(list)
    graph[0] = [0]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    # print(graph, len(graph))

    def dfs(node, visited):
        global count
        visited[node] = True
        count += 1
        for i in graph[node]:
            if not visited[i]:
                dfs(i, visited)

    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        count = 0
        visited = [False] * (n + 1)
        dfs(1, visited)
        answer.append(abs(n - count - count))
        graph[v1].append(v2)
        graph[v2].append(v1)

    return min(answer) if answer else 0


print(solution(n=9, wires=[[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
