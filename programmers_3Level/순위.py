# n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다.
# 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다.
# 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다.
# 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

# 선수의 수 n, 경기 결과를 담은 2차원 배열 results
# 정확하게 순위를 매길 수 있는 선수의 수를 return

from collections import defaultdict


def solution(n, results):
    answer = 0
    wins = defaultdict(set)
    loses = defaultdict(set)

    # 1선수당 승리, 패배로 구성하기.
    for a, b in results:
        wins[a].add(b)
        loses[b].add(a)

    print('승리', wins)
    print('패배', loses)

    for i in range(1, n + 1):
        # print(f'{i}번 선수')

        # 각 번호의 승리, 패배를 모두 채워넣어주고
        # 마지막에 승리와 패배의 개수가 (n-1)개면 순위를 명확히 알 수 있는 번호다.

        # 2번이 제친 목록을 자식의 패배 목록에 넣어준다.
        for win in wins[i]:
            loses[win].update(loses[i])

        # 2번이 이기지 못한 목록을 부모의 승리 목록에 넣어준다.
        for lose in loses[i]:
            wins[lose].update(wins[i])

    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1

    return answer


print(solution(n=5, results=[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
