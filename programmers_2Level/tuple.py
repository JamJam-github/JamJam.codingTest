# 튜플

import re
from collections import Counter


def solution(s):
    answer = []

    s = s.replace('}}', '').replace('{{', '').split('},{')
    # print(s)

    s.sort(key=len)
    # print(s)

    for i in s:
        t = i.split(',')
        for j in t:
            if not j in answer:
                answer.append(j)

    return list(map(int, answer))


print(solution(s="{{4,2,3},{3},{2,3,4,1},{2,3}}"))


# 다른 사람의 풀이
# Counter 함수로 각 숫자의 개수를 세기
# 가장 빈도수가 높은 숫자 순으로 출력

def solution_other(s):
    # print(re.findall('\d+', s))

    # 연속된 숫자들을 추출해서 list로 리턴 : re.findall()
    # \d+ 는 1회 이상 반복되는 숫자들에 대한 패턴
    # \d 는 1개 단위 숫자
    s = Counter(re.findall('\d+', s))
    # print('s::', s)
    # print('s.items::', s.items())
    # print('sorted::', sorted(s.items(), key=lambda x: x[1], reverse=True))

    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

# print(solution_other(s="{{4,2,3},{3},{2,3,4,1},{2,3}}"))
