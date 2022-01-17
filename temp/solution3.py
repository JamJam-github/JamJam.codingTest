# (02) 리스트에서 원소 찾아내기
# 인자로 주어지는 리스트 L 내에서,
# 또한 인자로 주어지는 원소 x 가 발견되는 모든 인덱스를 구하여 이 인덱스들로 이루어진 리스트를
# 반환하는 함수 solution 을 완성하세요.

L = [64, 72, 83, 72, 54]
x = 72


def solution(L, x):
    answer = [idx for idx, value in enumerate(L) if x == value]
    if answer:
        return answer
    else:
        return [-1]


print(solution(L, x))
