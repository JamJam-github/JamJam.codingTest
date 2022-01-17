class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    # pos 번째 위치에 newNode를 삽입한다.
    def insertAt(self, pos, newNode):
        # pos는 1부터 시작한다.
        # 0이 들어오거나 over 되는 숫자 (예외 사항)
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        # 맨 앞에 넣을 경우 [newNode]->[prev(head)]
        # newNode는 head로 지정
        # 현재 head를 newNode의 링크에 할당
        if pos == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            # 맨 뒤에 넣을 경우 [prev(tail)]->[newNode]
            # tail을 prev로 지정 (* tail은 마지막을 가리키고 있으니 앞에서부터 찾아올 필요가 없음)
            if pos == self.nodeCount + 1:
                prev = self.tail

            # 중간에 넣을 경우 [prev]->[newNode]->[prev.next]
            # (pos-1) 번째 Node를 가져와 prev로 지정
            else:
                prev = self.getAt(pos - 1)

            ## 순서 중요
            # newNode 링크를 부여하고 이전 노드와 연결시킨다.
            newNode.next = prev.next
            prev.next = newNode

        # 맨 뒤에 넣었을 경우 tail로 지정
        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    def getLength(self):
        return self.nodeCount

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        curr = self.getAt(pos)
        # 맨 앞 노드 삭제
        if pos == 1:
            # 유일한 노드인 경우 curr.next
            if pos == self.nodeCount:
                self.head, self.tail = None, None
            else:
                self.head = curr.next

        # 중간 노드 삭제
        else:
            prev = self.getAt(pos-1)
            # 맨 뒤 노드 삭제
            if pos == self.nodeCount:
                self.tail = prev
                # ... -> prev -> curr -> None 연결 순서이기 때문에 처리 필수
            prev.next = curr.next

        self.nodeCount -= 1
        return curr.data

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount


a = Node(67)
b = Node(34)
c = Node(28)
L = LinkedList()
print(L)

L.insertAt(1, a)
print(L)
L.insertAt(2, b)
print(L)
L.insertAt(1, c)
print(L)