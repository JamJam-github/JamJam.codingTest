# 피로도

from itertools import permutations


def solution(k, dungeons):
    answer = []
    # pmt = list(permutations(dungeons, len(dungeons)))
    n = len(dungeons)
    for i in permutations(range(n)):
        somo = k
        count = 0
        # print(i)
        for j in i:
            if dungeons[j][0] > somo or somo < 0:
                # print('소모 피로도 부족::', somo)
                break

            somo -= dungeons[j][1]
            count += 1

        answer.append(count)

    return max(answer) if answer else -1


print(solution(k=80, dungeons=[[80, 20], [50, 40], [30, 10]]))
