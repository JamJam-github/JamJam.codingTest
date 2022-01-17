# (20) 이진 탐색 트리의 원소 삽입 연산 구현

# 이진 탐색 트리
# 왼쪽 서브트리에 있는 데이터는 현재 노드의 값보다 작고
# 오른쪽 서브트리에 있는 데이터는 현재 노드의 값보다 크다.
# 중복된 데이터는 없는 것으로 간주한다.

class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key, data):
        # self가 큰 경우 왼쪽 서브트리로 향한다
        # 도달한 경우 노드를 새로 추가
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        elif self.key < key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else:
            raise KeyError

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


class BinSearchTree:

    def __init__(self):
        self.root = None

    # 새로운 원소 삽입
    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


def solution(x):
    return 0
