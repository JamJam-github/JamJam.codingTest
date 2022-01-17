# 완전탐색
# Level 1) 모의고사

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

import math

A = [1, 2, 3, 4, 5]
B = [2, 1, 2, 3, 2, 4, 2, 5]
C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

answers = [1, 3, 2, 4, 2]
A *= math.ceil(len(answers) / len(A))
B *= math.ceil(len(answers) / len(B))
C *= math.ceil(len(answers) / len(C))

answer = {}
for i, v in enumerate(answers):
    if v == A[i]:
        answer[1] = answer.get(1, 0) + 1

    if v == B[i]:
        answer[2] = answer.get(2, 0) + 1

    if v == C[i]:
        answer[3] = answer.get(3, 0) + 1

print(f'점수 = {answer}')

# for i, v in enumerate(answer):
#     print("enumerate 결과: ", i, v)
#
# for i, v in answer.items():
#     print("items 결과: ", i, v)

answer = sorted([i for i, v in answer.items() if max(answer.values()) == v])
print(answer)

# 다른 사람의 풀이
# -- 패턴1, 2, 3에 대해서 리스트를 늘리기 보다
# 패턴의 끝에 도달하게되면 다시 처음 패턴을 비교할 수 있도록
# 나눈 나머지 연산자(%)를 사용하자. --
# pattern1, pattern2, pattern3 = [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]
# score = [0, 0, 0]
# for idx, answer in enumerate(answers):
#     if answer == pattern1[idx % len(pattern1)]:
#     score[0] += 1
#  결론) score = [5, 1, 2] 인 경우
#  max(score) 값과 score 배열이 일치하는 index를 최종 result 리스트로 반환.

