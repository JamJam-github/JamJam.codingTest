# 기능개발

# 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
# 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고,
# 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

# progresses=[93, 30, 55], speeds=[1, 30, 5]
# 첫 번째 기능은 93% 완료되어 있고 하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.
# 두 번째 기능은 30%가 완료되어 있고 하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다.
# 하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포됩니다.
# 세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다.
# 따라서 7일째에 2개의 기능, 9일째에 1개의 기능이 배포됩니다.

import math


def solution(progresses, speeds):
    answer = []
    released = []
    for p, s in zip(progresses, speeds):
        released.append(math.ceil((100 - p) / s))

    print(f'개발일 :: {released}')

    # front는 우선순위 배포될 released의 기준일
    front = 0
    for i in range(len(released)):
        if released[i] > released[front]:
            answer.append(i - front)
            front = i
    answer.append(len(released) - front)
    return answer


print(solution(progresses=[93, 30, 55], speeds=[1, 30, 5]))


# 다른 사람의 풀이
# Q = [[배포일, 배포기능개수]]
# Q[-1] 리스트의 마지막  Q[-1][0] 리스트의 마지막에 배포일

def solution_other(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        # -((p - 100) // s) 은 math.ceil과 같은 동작. 음수에서 내림은 절대값이 커진다.
        if len(Q) == 0 or Q[-1][0] < -((p - 100) // s):
            Q.append([-((p - 100) // s), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]
