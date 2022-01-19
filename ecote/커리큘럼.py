# 위상 정렬
# 각 온라인 강의는 선수 강의가 있을 수 있다.
# 총 N개의 강의를 듣고자 할 때, 모든 강의는 1번부터 N번까지의 번호를 가진다.
# 또한, 동시에 여러 개의 강의를 들을 수 있다.
# 듣고자 하는 N개의 강의 정보가 주어졌을 때, 걸리는 최소 시간을 각각 출력하시오.
# (1 <= N <= 500), 각 강의번호는 1부터 N까지 구성되며 각 줄은 -1로 끝난다.
from collections import deque
from collections import defaultdict


def solution(n, array):
    # 1. 진입 차수와 방향그래프를 생성해준다.
    # 2. 진입 차수가 0인 노드를 큐에 넣어주는 작업
    # 3. 큐가 빌 때까지 반복한다.
    #    3-1. 큐에서 원소를 꺼내 해당 노드에 연결된 간선을 제거한다.
    #    3-2. 새롭게 진입 차수가 0인 노드를 큐에 넣어주는 작업
    # 4. 큐에서 나온 데이터는 위상 정렬을 수행한 결과다.
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    time = [0] * (n + 1)

    # 1.
    for i in range(1, n + 1):
        time[i] = array[i-1][0]
        for j in array[i-1][1:-1]:
            indegree[i] += 1
            graph[j].append(i)
    print('graph::', graph)
    print('indegree::', indegree)

    queue = deque()
    # 2.
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    # 3.
    result = time[:]
    while queue:
        node = queue.popleft()

        # 3-1.
        for i in graph[node]:
            indegree[i] -= 1
            result[i] = max(result[i], result[node] + time[i])

            # 3-2.
            if indegree[i] == 0:
                queue.append(i)

    return result[1:]


print(solution(n=5, array=[[10, -1], [10, 1, -1], [4, 1, -1], [4, 3, 1, -1], [3, 3, -1]]))
