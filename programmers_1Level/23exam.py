# 두 개 뽑아서 더하기
# 정수 배열 numbers가 주어집니다.
# numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에
# 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
# 풀이: 하나의 리스트에서 모든 조합을 계산을 해야 한다면, permutations, combinations을 사용
#      두개 이상의 리스트에서 모든 조합을 계산해야 한다면, product를 사용


from itertools import combinations


def solution(numbers):
    l = list(combinations(numbers, 2))
    s = [sum(i) for i in l]
    return sorted(list(set(s)))


print(solution([5, 0, 2, 7]))
