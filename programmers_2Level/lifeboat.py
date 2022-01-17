# 구명보트

# 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.
# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.
# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때,
# 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 구하라.

import math


def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    n = len(people)

    left = 0
    right = n - 1
    while left <= right:
        if people[left] <= limit // 2:
            answer += math.ceil((right - left + 1) / 2)
            break

        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            left += 1
        answer += 1

    return answer


# print(solution(people=[70, 50, 80, 50], limit=100))
print(solution(people=[70, 80, 50], limit=100))


# 다른 사람의 풀이
# 맨 앞과 맨 뒤를 짝지어서 시작해서 짝이 지어진 경우 카운트
# 최종 사람 수에서 짝(2명) 지어진 사람을 제외하면 구명보트 사용 수

def solution(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b:
        if people[a] + people[b] <= limit:
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
