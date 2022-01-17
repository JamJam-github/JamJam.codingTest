# 탐욕법 - 현재 상황에서 당장 좋은 것만 고르는 방법

# N이 1이 될때까지 수행해야 하는 횟수의 최소값
# 1 <= N <= 100,000, 2 <= K <= 100,000
# 1) N - 1
# 2) N / K

# [문제 해결 아이디어]
# 주어진 N에 대해 최대한 많이 나누기를 수행하면 된다.
# N의 값을 줄일때 2이상의 수로 나누는 작업이 1을 빼는 작업보다 훨씬 많이 줄일 수 있다.


from collections import deque


def solution(n, k):
    answer = []
    queue = deque()

    count = 0
    number = n
    if number > 1:
        if number % k == 0:
            queue.append((number // k, count))
        else:
            queue.append((number - 1, count))

    while queue:
        value, count = queue.popleft()

        count += 1
        if value == 1:
            answer.append(count)
        else:
            if value % k == 0:
                queue.append((value // k, count))
            else:
                queue.append((value - 1, count))

    # print('1을 만드는 모든 작업의 수 ::', answer)
    return min(answer) if answer else 0


# print(solution(n=25, k=5))
# print(solution(n=25, k=3))
# print(solution(n=17, k=4))
# print(solution(n=2, k=2))


# 다른 풀이

def other_solution(n, k):
    result = 0

    while True:
        # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
        # n이 k로 나누어 떨어지지 않을때 가장 가까운 수로 만들어주는 것임
        # 결국 target은 k로 나누어 떨어지는 수가 된다.
        target = (n // k) * k
        # 1을 빼주는 연산을 몇번 수행할지 결과에 추가
        result += (n - target)
        n = target
        # print(f'target = {target}, result = {result}')
        
        # n이 k보다 작으면 (더 이상 나눌 수 없음) 반복문 탈출
        if n < k:
            break
        
        # n을 k로 나누고 한번 수행한 것 추가
        result += 1
        n //= k

    result += (n - 1)
    return result

print(other_solution(n=25, k=3))
