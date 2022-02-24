# 0으로 설정된 카운터 리스트에서 두 가지 작업이 가능하다.
# 1) A[K] = X 에서 X 값이 N보다 작거나 같으면 카운터[X]는 1 증가
# 2) A[K] 값이 N + 1 값과 같으면 카운터의 MAX 값으로 모든 카운터를 적용

# large_random 에서 속도 터짐
# max(리스트)를 사용하지 않고 변수로 가지고 있어야하고,
# 모든 카운터 적용 시 새로 배열을 만들지 않고 값을 따로 저장해두었다가 하나씩 반영해주기

def solution(N, A):
    counter = [0 for i in range(N)]
    max_num, save_num = 0, 0
    for i in range(len(A)):
        x = A[i]
        # print(f'A[{i}] = {x}, counter = {counter}')

        if x <= N:
            # 현재 위치 동기화 작업
            if counter[x - 1] < save_num:
                counter[x - 1] = save_num
            counter[x - 1] += 1
            max_num = max(max_num, counter[x - 1])
        else:
            save_num = max_num
    # print(counter)

    # 나머지 동기화 작업
    for i in range(len(counter)):
        if counter[i] < save_num:
            counter[i] = save_num

    return counter