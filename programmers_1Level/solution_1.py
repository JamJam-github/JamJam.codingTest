# 코딩테스트 고득점 Kit
# 해시 - Key-value쌍으로 데이터를 빠르게 찾아보세요.
# Level 1) 완주하지 못한 선수


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    dict = {}
    for part in participant:
        dict[part] = dict.get(part, 0) + 1

        print(f'생성 후 dict :: {dict}')

    for comp in completion:
        dict[comp] -= 1

        print(f'조정 후 dict :: {dict}')

    dnf = [k for k, value in dict.items() if value > 0]

    return dnf[0]


print(solution(participant, completion))

# 다른 사람의 풀이
# Python - collections의 Counter 함수를 사용해서 쉽게 풀 수 있음
# import collections
# answer = collections.Counter(participant) - collections.Counter(completion)
