# 프린터
from collections import deque


def solution(priorities, location):
    answer = 0

    # arr = []
    # for i, v in enumerate(priorities):
    #     arr.append((v, i))
    # queue = deque(arr)
    queue = deque([(v, i) for i, v in enumerate(priorities)])

    result = []
    while queue:
        priority, idx = queue.popleft()

        if queue and priority < max(queue)[0]:
            # print(f'{idx}번째 {priority} < {max(queue)[0]} 낮기때문에 다시 삽입')
            # 우선순위가 낮아서 다시 삽입
            queue.append((priority, idx))
            # pass
        else:
            # print(f'우선순위가 높아서 출력, 현재 큐 :: {queue}')
            answer += 1
            if idx == location:
                return answer
            # result.append((priority, idx))

    # print('출력 순서:', result)
    # for i in range(len(result)):
    #     print(f'result[i][1] = {result[i][1]}')
        # if result[i][1] == location:
        #     return i+1
    return answer


print(solution(priorities=[1, 1, 9, 1, 1, 1], location=0))
print(solution(priorities=[2, 1, 3, 2], location=2))
print(solution(priorities=[1, 1, 1, 1, 1, 1], location=3))
print(solution(priorities=[2], location=0))
