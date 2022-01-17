# 이분 탐색
# n명이 입국심사를 위해 줄을 서서 기다리고 있습니다.
# 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다.
# 모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.
#
# 입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times

def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n  # 최대로 걸리는 시간

    while left <= right:
        mid = (left + right) // 2  # 중간 시간
        people = 0

        for time in times:
            people += mid // time

            if people >= n:
                break

        # 주어진 인원보다 더 많이 처리되어 시간을 줄여서 다시 처리
        if people >= n:
            answer = mid
            # print(people, mid)
            right = mid - 1
        # 주어진 인원보다 적게 처리되어 시간을 늘려서 다시 처리
        else:
            left = mid + 1

    return answer


print(solution(n=6, times=[7, 10]))
