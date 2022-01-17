# 더 맵게
# 모든 음식의 스코빌 지수를 K 이상 만들기 위해
# 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.
# [방법] 섞은 스코빌 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 구하세요.

import heapq


# def scoville_sort(scoville):
#     heapq.heapify(scoville)
#     n1 = heapq.heappop(scoville)
#     n2 = heapq.heappop(scoville)
#     return n1, n2, scoville

# 최소힙, 우선순위 큐를 사용해서 루트노드는 항상 가장 작은 값을 유지하고
# 루트 노드[0]가 K 지수 이상으로 만들면 된다.
# heappop, heappush의 경우 즉시 heap 정렬을 자동으로 해줌
def solution1(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    # print('init heap sort', scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        n1 = heapq.heappop(scoville)
        n2 = heapq.heappop(scoville)
        new = n1 + (n2 * 2)
        heapq.heappush(scoville, new)
        answer += 1
    return answer

    # [효율성 실패한 코드] sort() 사용하지 않고, 스코빌 개수만큼 heapify를 실행해서
    # heapify 최초 1번 실행 후 pop & push 되도록 구현하기

    # for i in range(len(scoville)):
    #     if len(scoville) == 1:
    #         return -1
    #
    #     n1, n2, scoville = scoville_sort(scoville)
    #     new = n1 + (n2 * 2)
    #     heapq.heappush(scoville, new)
    #
    #     if min(scoville) >= K:
    #         return i + 1
    #
    # return -1


print(solution1(scoville=[1, 2, 3], K=1))
