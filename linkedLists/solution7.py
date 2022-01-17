# (07) 연결 리스트 순회

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    # pos번째 data 를 return 하는 함수
    def getAt(self, pos):
        if pos <= 0 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        bins = []
        node = self.head
        while node != None:  # 헤드가 있는 동안
            bins.append(node.data)  # 데이터를 넣는다.
            node = node.next  # 연결을 재정의한다.
        return bins  # 리스트 출력한다.
