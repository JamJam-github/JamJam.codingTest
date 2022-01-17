# 하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다.
# 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다.
# 가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.

# A → C → B의 순서로 처리하면 각 작업의 요청부터 종료까지 걸린 시간의 평균은
# 9ms(= (3 + 7 + 17) / 3)가 됩니다.
#
# 각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때,
# 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지
# return 하도록 solution 함수를 작성해주세요.

import heapq


def solution(jobs):
    answer, end_time, i = 0, 0, 0
    start = -1
    queue = []

    # (요청 시간 <= 총 종료 시간) and 작업 소요시간이 적은 순으로 작업을 처리해줘야 한다.
    # (요청 시간 <= 총 종료 시간) 일치하는 작업을 heap(최소힙)에 저장하면 소요시간이 적은 순서대로 처리될 것
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= end_time:
                heapq.heappush(queue, [job[1], job[0]])  # 소요시간 순서대로 넣기

        if len(queue):
            cur_time, cur_start = heapq.heappop(queue)
            start = end_time
            end_time += cur_time
            answer += end_time - cur_start
            i += 1
        else:
            end_time += 1

        # cur_start, cur_time = heapq.heappop(queue)
        # end_time = answer[-1] + cur_time - cur_start
        # answer.append(end_time)

        # nodes = sorted([i for i in jobs if i[0] <= end_time], key=lambda x: x[1])
        # for next_node in nodes:
        #     heapq.heappush(queue, next_node)

    return int(answer / len(jobs))


print(solution(jobs=[[0, 3], [1, 9], [2, 6]]))
