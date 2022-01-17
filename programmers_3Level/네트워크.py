# 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고,
# 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때
# 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다.
# 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers
from collections import defaultdict, deque


def solution(n, computers):
    answer = 0

    # graph = defaultdict(list)
    # for idx, value in enumerate(computers):
    #     for idx2, value2 in enumerate(computers[idx]):
    #         # 자기 자신 제외하고, 연결 표시 1인 경우
    #         if idx != idx2 and value2:
    #             graph[idx+1].append(idx2+1)

    def dfs(node):
        visited[node] = True
        for j in range(n):
            # 연결 표시 1인 경우 and 미방문 상태인 경우 탐색
            if computers[node][j] and not visited[j]:
                dfs(j)

    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            # 처음 방문할때만 카운트 처리, 내부에서 연결된 네트워크 방문처리하기
            dfs(i)
            answer += 1
    return answer


print(solution(n=3, computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(n=3, computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))