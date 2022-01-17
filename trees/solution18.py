# (19) 이진 트리의 넓이 우선 순회
# 이진 트리를 구현한 클래스인 class BinaryTree 에 대하여
# 넓이 우선 순회 (breadth first traversal) 를 구현하는 메서드 bft() 를 완성하세요.

class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def bft(self):
        traversal = []
        q = ArrayQueue()
        
        # 주어진 트리가 비어있지 않으면 루트노드를 빈 Queue 추가
        if self.root:
            q.enqueue(self.root)

        # q가 비어있지 않는 동안, q 추출 -> 추출한 노드방문 -> 자식여부에 따라 q에 추가
        while not q.isEmpty():
            curr = q.dequeue()
            traversal.append(curr.data)
            if curr.left:
                q.enqueue(curr.left)
            if curr.right:
                q.enqueue(curr.right)

        return traversal


def solution(x):
    return 0
