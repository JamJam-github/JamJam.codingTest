# 탐욕법(Greedy)
# 부분적인 최적해가 전체적인 최적해가 되는 마법!
# Level 1) 체육복

n = 5
lost = [2, 4]
reserve = [3]


def solution(n, lost, reserve):
    intersection = len(set(lost) & set(reserve))
    answer = n - len(lost) + intersection

    lost2 = list(set(lost) - set(reserve))
    reserve2 = list(set(reserve) - set(lost))

    lost_flag = [0] * len(lost2)
    for r in reserve2:
        for i, v in enumerate(lost2):
            if r - 1 == v or r + 1 == v:
                if lost_flag[i]:
                    pass
                else:
                    lost_flag[i] = 1
                    answer += 1
                    break

    return answer


print(solution(n, lost, reserve))
print()

# 다른 사람의 풀이
# 차집합을 각각 구하고
# _reserve = [r for r in reserve if r not in lost]
# _lost = [l for l in lost if l not in reserve]
# 반복문 _reserve 를 기준으로 _lost 내 조건에 일치하는 값을 찾을 경우,
# 리스트에서 del 하는 형태로 가자. _lost.remove(f)
# 최종 n명에서 _lost (해결하지 못한 사람)명을 제외하면 된다.
