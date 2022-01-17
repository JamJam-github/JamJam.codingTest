# 프로그램은 2차원 가상 벽면에 기둥과 보를 이용한 구조물을 설치할 수 있는데,
# 기둥과 보는 길이가 1인 선분으로 표현되며 다음과 같은 규칙을 가지고 있습니다.
# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

# 2차원 벽면은 n x n 크기 정사각 격자 형태이며, 각 격자는 1 x 1 크기입니다.
# 맨 처음 벽면은 비어있는 상태입니다. (5 <= n <= 100)

# build_frame의 원소는 [x, y, a, b]형태입니다.
# x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
# a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
# b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.
# 벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다.
# 바닥에 보를 설치 하는 경우는 없습니다.

# return 하는 배열의 원소는 [x, y, a] 형식입니다.
# return 하는 배열은 x좌표 기준으로 오름차순 정렬하며,
# x좌표가 같을 경우 y좌표 기준으로 오름차순 정렬해주세요.
# x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다.

def build_impossible(ans):
    gidung, bo = 0, 1
    for x, y, a in ans:
        if a == gidung:
            if y != 0 and (x, y - 1, gidung) not in ans and (x - 1, y, bo) not in ans and (x, y, bo) not in ans:
                return True
        else:
            if (x, y - 1, gidung) not in ans and (x + 1, y - 1, gidung) not in ans and not (
                    (x - 1, y, bo) in ans and (x + 1, y, bo) in ans):
                return True

    return False


def solution(n, build_frame):
    answer = set()

    # build_frame 명령을 다 수행해야 하는데,
    # 기둥 설치시 1) 맨 밑 2) 밑에 기둥이 있을때 3) 왼쪽(해당 점)에 보가 있을때 4) 해당 점(오른쪽 편을 향하는)에 보가 있을때
    # 보 설치시 1) 아래 기둥이 있을때 2) 오른쪽(보 설치하려는 아래의 오른쪽)에 기둥이 있을때 3) 양 옆에 보가 있을때
    for x, y, a, build in build_frame:
        if build:
            # 넣고, 체크해서 설치가 불가능하면 목록에서 지워준다.
            answer.add((x, y, a))
            if build_impossible(answer):
                answer.remove((x, y, a))
        else:
            # 지우고, 체크해서 삭제가 불가능하면 다시 넣어준다.
            answer.discard((x, y, a))
            if build_impossible(answer):
                answer.add((x, y, a))
    answer = map(list, answer)
    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))


print(solution(n=5, build_frame=[[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1],
                                 [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
