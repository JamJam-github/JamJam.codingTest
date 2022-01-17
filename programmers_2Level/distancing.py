# 거리두기 확인하기

def check(place):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for x in range(len(place)):
        for y in range(len(place[x])):
            result = True
            count = 0

            # P이면 상하좌우에 P가 있으면 안된다.
            if place[x][y] == 'P':
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # 공간을 벗어날 경우 무시
                    if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                        continue

                    if place[nx][ny] == 'P':
                        result = False
                        break

            # O이면 상하좌우에 P가 1개 이하여야 된다.
            if place[x][y] == 'O':
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # 공간을 벗어날 경우 무시
                    if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                        continue

                    if place[nx][ny] == 'P':
                        count += 1

            if not result or count > 1:
                return False

    return True


def solution(places):
    answer = []
    for place in places:
        chk = check(place)
        if chk:
            answer.append(1)
        else:
            answer.append(0)
    return answer


print(solution(places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                       ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                       ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                       ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                       ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
# print(solution(places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]]))
