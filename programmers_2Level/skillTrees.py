# 스킬트리

from collections import defaultdict


def solution(skill, skill_trees):
    answer = 0

    # 사용안해도 되네.
    # dic = defaultdict(int)
    # idx = 1
    # for i in skill:
    #     dic[i] += idx
    #     idx += 1

    for i in skill_trees:
        tree = ''
        for j in i:
            # if dic.get(j, 0):
            if j in skill:
                tree += j

        if tree == skill[:len(tree)]:
            answer += 1

    return answer


print(solution(skill="CBD", skill_trees=["BACDE", "CBADF", "AECB", "BDA"]))
