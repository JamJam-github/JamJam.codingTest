# 곤경에 빠진 카카오 프렌즈를 위해
# 이진트리를 구성하는 노드들의 좌표가 담긴 배열 nodeinfo가 매개변수로 주어질 때,
# 노드들로 구성된 이진트리를 전위 순회, 후위 순회한 결과를
# 2차원 배열에 순서대로 담아 return 하도록 solution 함수를 완성하자.

# python 재귀호출 범위를 늘려야 런타임 오류가 해결된다. (기본값 1000)
import sys

class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x  # 작은게 true 값으로 오름차순
        return self.y > other.y  # y가 큰게 true 값으로 내림차순


# 이진트리 노드 삽입
def addNode(parent, child):
    # 항상 기준은 루트에서 시작하며
    # 부모보다 작으면 왼쪽, 크면 오른쪽
    # 링크가 없을 경우 최초 부여하고,
    # 링크가 있을 경우 재귀적으로 내려가면서 할당해준다.
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            addNode(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            addNode(parent.right, child)


def preorder(ans, node):
    if node is None:
        return

    ans.append(node.id)
    preorder(ans, node.left)
    preorder(ans, node.right)


def postorder(ans, node):
    if node is None:
        return
    postorder(ans, node.left)
    postorder(ans, node.right)
    ans.append(node.id)
    return ans


def solution(nodeinfo):
    sys.setrecursionlimit(1500)
    n = len(nodeinfo)
    # [id, x, y, left, right] 형태로 만들고 y 내림차순, x 오름차순으로 정렬
    nodeList = []
    for i in range(n):
        # nodeList.append([i + 1, nodeinfo[i][0], nodeinfo[i][1], None, None])
        nodeList.append(Node(i + 1, nodeinfo[i][0], nodeinfo[i][1]))
    # print('nodeList::', nodeList)

    nodeList.sort()  # __lt__ 적용
    root = nodeList[0]  # 루트 노드
    for i in range(1, n):
        addNode(root, nodeList[i])

    # 이진트리 순회
    # 전위순회 (self -> left -> right)
    # 후위순회 (left -> right -> self)
    # answer = traverse(root, nodeList)
    answer = [[], []]
    preorder(answer[0], root)
    postorder(answer[1], root)
    return answer


print(solution(nodeinfo=[[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
