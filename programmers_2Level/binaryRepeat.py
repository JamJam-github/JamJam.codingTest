# 이진 변환 반복하기

# 0과 1로 이루어진 어떤 문자열 x에 대한 이진 변환
# 1) x에서 0을 제거한다.
# 2) x의 길이를 c라고 하면, c를 2진법으로 표현한 문자열로 바꾼다.
# 1, 2번 과정을 x가 1이 될 때까지 반복한다.
# x = "0111010" -> "1111" -> c = 4, 4를 2진법 변환 -> format(4, 'b') '100'


def solution(s):
    zero, totalCnt = 0, 0
    while s != '1':
        totalCnt += 1
        length = len(s)
        s = s.replace('0', '')
        zero += (length - len(s))
        s = format(len(s), 'b')
    return [totalCnt, zero]


print(solution(s="110010101001"))
print(solution(s="01110"))
print(solution(s="1111111"))
