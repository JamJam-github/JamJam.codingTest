# DFS/BFS -> Stack 사용
# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다.
# 항상 "ICN" 공항에서 출발합니다.

# tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
from collections import defaultdict


def solution(tickets):
    ticket = defaultdict(list)
    for a, b in sorted(tickets, key=lambda x: (x[0], x[1])):
        ticket[a].append(b)
    # print(ticket)

    stack = ['ICN']
    visited = []
    while stack:
        airport = stack[-1]
        # print('현재 스택에서 꺼내온 값::', airport)

        if ticket.get(airport, ''):
            nxt_airport = ticket[airport].pop(0)
            stack.append(nxt_airport)
        else:
            visited.append(stack.pop())

    return visited[::-1]


print(solution(tickets=[["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["COO", "BOO"]]))
# print(solution(tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))

# 딕셔너리 정렬
# 키를 가져와서 해당 값(리스트) 정렬
# for r in routes.keys():
#     routes[r].sort(reverse=True)

# 다른 사람의 풀이
def dfs(graph, N, key, footprint):
    # print(footprint)

    if len(footprint) == N + 1:
        return footprint

    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)

        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)

        graph[key].insert(idx, country)

        if ret:
            return ret


def solution_other(tickets):
    graph = defaultdict(list)
    N = len(tickets)

    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()

    answer = dfs(graph, N, "ICN", ["ICN"])
    return answer

