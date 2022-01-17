# [1차] 다트 게임

dartResult = "1D2S#10S"


def solution(dartResult):
    stack = []
    dic = {'S': 1, 'D': 2, 'T': 3}
    dartResult = dartResult.replace('10', 'K')
    for i in dartResult:
        if i.isdigit() or i == 'K':
            stack.append(int(i.replace('K', '10')))
        elif i.isalpha():
            stack[-1] **= dic[i]
        elif i == '#':
            stack[-1] *= -1
        elif i == '*':
            stack[-1] *= 2
            if len(stack) > 1:
                stack[-2] *= 2

    return sum(stack)


print(solution(dartResult))

# 다른 사람의 풀이
# 정규식으로 풀이, 다트게임 형태는 숫자|문자|특수문자로 되어있음.
# p = re.compile('(\d+)([SDT])([*#]?)')
# p.findall('(\d+)([SDT])([*#?])') 튜플 형태로 쪼개서 구하기
