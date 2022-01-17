# I 숫자 : 큐에 주어진 숫자를 삽입합니다.
# D 1	: 큐에서 최댓값을 삭제합니다.
# D -1	: 큐에서 최솟값을 삭제합니다.
import heapq


def solution(operations):
    heap = []
    # max_heap = []
    # min_heap = []
    for oper in operations:
        if oper[0] == 'I':
            # heapq.heappush(max_heap, (-int(oper[2:]), int(oper[2:])))
            # heapq.heappush(min_heap, int(oper[2:]))
            heapq.heappush(heap, int(oper[2:]))
        # elif min_heap:
        elif heap:
            # 최소값 삭제
            if int(oper[2:]) < 0:
                heapq.heappop(heap)
                # heapq.heappop(min_heap)
                # max_heap.pop()
            else:
                # heap 리스트에서 가장 큰 n개의 수를 뽑아내고
                # 가장 큰 수(인덱스 첫번째)를 제외하고 다시 heap 리스트를 구성한다.
                # heapify 최소힙 정렬
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
                # heapq.heappop(max_heap)
                # min_heap.pop()

    # print('>', max_heap)
    # print('>', min_heap)
    # return [max_heap[0][1], min_heap[0]] if max_heap else [0, 0]
    # print(heap)
    return [max(heap), heap[0]] if heap else [0, 0]


print(solution(operations=["I 16", "D 1"]))
print(solution(operations=["I 7", "I 5", "I -5", "D -1"]))
