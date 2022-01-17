# (22) 최대 힙에 새로운 원소 삽입

# 최대힙: 부모가 자식보다 항상 큰 값을 가진다. 자식의 왼쪽 오른쪽의 크기는 상관없다.
# 노드 번호 m을 기준으로 왼쪽 자식은 2 * m, 오른쪽 자식은 2 * m + 1, 부모 노드는 m // 2

# 구현 순서
# 1) 리스트 마지막에 삽입한다.
# 2) 마지막 번호(ex 6번)의 부모 번호(ex 6//2번)와 비교해서 부모보다 크면 swap
# 3) 루트 번호(1번)까지 비교를 반복하기.

class MaxHeap:

    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)
        l = len(self.data) - 1
        print(f'현재 len ::{l}')
        
        # 부모보다 자식이 큰 경우에 위로이동
        while l > 1:
            print(f'자식 {self.data[l]}, 부모 {self.data[l // 2]}')
            if self.data[l//2] < self.data[l]:
                self.data[l // 2], self.data[l] = self.data[l], self.data[l // 2]
                l = l // 2
            else:
                break

        return True

heap = MaxHeap()
heap.insert(20)
heap.insert(6)
heap.insert(12)
heap.insert(2)
heap.insert(4)
print(heap.data)
print("##################")
heap.insert(30)
heap.insert(3)
print(heap.data)