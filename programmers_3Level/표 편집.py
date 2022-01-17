# 표의 행을 선택, 삭제, 복구하는 프로그램을 작성하는 과제를 맡았습니다.
# "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
# "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
# "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
# "Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.


from collections import defaultdict


def solution(n, k, cmd):
    answer = ["O" for _ in range(n)]
    linked_list = defaultdict(list)

    for i in range(1, n + 1):
        linked_list[i].append(i - 1)
        linked_list[i].append(i + 1)
    print(linked_list)
    
    stack = []
    k += 1

    for str in cmd:
        if str[0] == "D":
            for _ in range(int(str[2:])):
                k = linked_list[k][1]  # node.next

        elif str[0] == "U":
            for _ in range(int(str[2:])):
                k = linked_list[k][0]  # node.prev

        elif str[0] == "C":
            prev, next = linked_list[k]
            stack.append([prev, next, k])
            answer[k - 1] = "X"

            # 마지막 행이 삭제되는 경우 이전행을 바라보도록
            if next == n + 1:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            # removed 처리하고 양쪽 링크를 변경
            # 이전 노드는 다음 노드를 바라보고
            # 다음 노드는 이전 노드를 바라보도록
            if prev == 0:
                linked_list[next][0] = prev
            elif next == n + 1:
                linked_list[prev][1] = next
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev

        elif str[0] == "Z":
            prev, next, now = stack.pop()
            answer[now - 1] = "O"

            if prev == 0:
                linked_list[next][0] = now
            elif next == n + 1:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[next][0] = now

    return "".join(answer)


def solution_temp(n, k, cmd):
    linked_list = {i: [None if i - 1 < 0 else i - 1, None if i + 1 == n else i + 1] for i in range(n)}
    o = ["O" for _ in range(n)]
    stack = []

    for c in cmd:
        if c[0] == 'D':
            for i in range(int(c[2:])):
                k = linked_list[k][1]  # node.next
        elif c[0] == 'U':
            for i in range(int(c[2:])):
                k = linked_list[k][0]  # node.prev
        elif c[0] == 'C':
            prev, next = linked_list[k]
            stack.append([prev, next, k])
            o[k] = 'X'

            # removed 처리하고 양쪽 링크를 변경
            # 이전 노드는 다음 노드를 바라보고
            # 다음 노드는 이전 노드를 바라보도록
            # 마지막 행을 삭제했을때 이전행 선택
            if prev:
                linked_list[prev][1] = next
            if next:
                linked_list[next][0] = prev
                k = next
            else:
                k = prev

        else:
            # Z 복구를 진행할때 K가 변화하지 않도록 한다.
            prev, next, now = stack.pop()
            o[now] = 'O'

            # 자기 자신의 링크를 복원해주기
            if prev:
                linked_list[prev][1] = now
            if next:
                linked_list[next][0] = now

    return "".join(o)


print(solution(n=8, k=2, cmd=["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(n=8, k=2, cmd=["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
