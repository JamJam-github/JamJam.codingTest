# 깊이/너비 우선 탐색(DFS/BFS)
# 타겟 넘버
# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.


from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque()
    # 첫 원소는 numbers[0] 를 다루며 양수이거나 음수 2가지로 시작한다.
    # 큐에 튜플 형태로 (계산 값, 인덱스) 만든다.
    queue.append((numbers[0], 0))
    queue.append((-1*numbers[0], 0))

    while queue:
        value, idx = queue.popleft()
        # 꺼낸 원소를 방문하고 인접한 다음 numbers[1] 값을 더해주거나 마이너스한 값을 넣어준다.
        # numbers 배열 길이만큼 실행한 누적 결과가 target과 일치하면 count 해주기
        idx += 1
        if idx < len(numbers):
            queue.append((value + numbers[idx], idx))
            queue.append((value - numbers[idx], idx))
        else:
            if value == target:
                answer += 1

    return answer


print(solution(numbers=[1, 1, 1, 1, 1], target=3))
