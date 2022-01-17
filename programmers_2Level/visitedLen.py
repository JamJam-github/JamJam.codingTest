# 방문 길이

# 캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다.
# 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.
# 게임 캐릭터가 움직인 길이는 9이지만, 캐릭터가 처음 걸어본 길의 길이는 7이 됩니다.

def solution(dirs):
    command = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    s = set()

    x, y = 0, 0
    for dir in dirs:
        nx, ny = x + command[dir][0], y + command[dir][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add(((nx, ny), (x, y)))
            s.add(((x, y), (nx, ny)))
            x, y = nx, ny

    return len(s) // 2


print(solution(dirs="ULURRDLLU"))
print('------------------------------')
print(solution(dirs="LULLLLLLU"))