# 전체 스테이지 개수 N
# 게임을 이용하는 사용자가 현재 멈춰있는 스테이지 번호 배열
# 실패율 = 스테이지에 머무는 사람 / 스테이지를 통과한 사람
# 실패율이 높은 스테이지부터 내림차순으로 리턴하세요.

def solution(N, stages):
    answer = []
    length = len(stages)
    for i in range(1, N + 1):
        stage_cnt = stages.count(i)
        # print(f'{i}번 스테이지 머무르는 사람 {stage_cnt}')

        if length == 0:
            fail = 0
        else:
            fail = stage_cnt / length

        answer.append((i, fail))
        length -= stage_cnt

    answer.sort(key=lambda x: x[1], reverse=True)
    return [i[0] for i in answer]


print(solution(N=5, stages=[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(N=4, stages=[4, 4, 4, 4, 4]))
