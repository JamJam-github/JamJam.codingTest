# (23) 최대 힙에서의 원소 삭제

# 구현 순서
# 1) 가장 큰 루트노드를 삭제(pop)한다.
# 2) 힙의 맨 마지막 원소를 루트로 보낸다.
# 3) maxHeapify(DownHeapify) 실행해서 부모와 자식 간 대소비교를 통해 큰 값을 위로 올린다.

class MaxHeap:

    def __init__(self):
        self.data = [None, 20, 10, 30, 7, 9, 21, 22, 6, 5, 14, 13, 19]

    def remove(self):
        print(f'삭제 전 self.data :: {self.data}')
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data

    def maxHeapify(self, i):
        print(f'maxHeapify self.data :: {self.data}')

        # 왼쪽 자식 (left child) 의 인덱스를 계산합니다.
        left = 2 * i
        # 오른쪽 자식 (right child) 의 인덱스를 계산합니다.
        right = 2 * i + 1
        smallest = i

        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if left <= len(self.data) and self.data[smallest] < self.data[left]:
            # 조건이 만족하는 경우, smallest 는 왼쪽 자식의 인덱스를 가집니다.
            smallest = left

        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if right <= len(self.data) and self.data[smallest] < self.data[right]:
            # 조건이 만족하는 경우, smallest 는 오른쪽 자식의 인덱스를 가집니다.
            smallest = right

        if smallest != i:
            print(f'교체될 자식: {self.data[smallest]}, 부모: {self.data[i]}')

            # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]

            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.maxHeapify(smallest)


def solution(x):
    return 0


heap = MaxHeap()
heap.remove()
