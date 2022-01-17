# [카카오 인턴] 수식 최대화

# 연산자에 대해 순열을 구하고
# 표현식을 리스트(숫자, 기호별) 분리하고
# 각 연산자 우선순위를 기준으로 반복하여 [0]번째 배열이 완성될때까지 계산한다.
from itertools import permutations


def oper(n1, n2, p):
    if p == '-':
        res = int(n1) - int(n2)
    elif p == '+':
        res = int(n1) + int(n2)
    else:
        res = int(n1) * int(n2)
    return res


def calc(number, np):
    arr = number.copy()
    for p in np:
        stack = []
        while len(arr) != 0:
            num = arr.pop(0)
            if num == p:
                stack.append(oper(stack.pop(), arr.pop(0), p))
            else:
                stack.append(num)
        arr = stack

    return abs(arr[0])


def solution(expression):
    answer = []

    dic = {}
    number = []
    strNum = ''
    for i in expression:
        if i.isdigit():
            strNum += i
        else:
            dic[i] = dic.get(i, 0) + 1

            if strNum:
                number.append(strNum)
                strNum = ''
                number.append(i)
    if strNum:
        number.append(strNum)

    nPr = list(permutations(dic))
    for np in nPr:
        print('np>>', np, number)
        answer.append(calc(number, np))

    return max(answer)


print(solution(expression="100-200*300-500+20"))
print(solution(expression="50*6-3*2"))


import re


# 다른 사람의 풀이
def solution_other(expression):
    op = [x for x in ['*', '+', '-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    print('op', op)

    # 숫자가 아닌 것을 기준으로 나눈다.
    ex = re.split(r'(\D)', expression)
    print('ex', ex)

    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp - 1] = str(eval(_ex[tmp - 1] + _ex[tmp] + _ex[tmp + 1]))
                _ex = _ex[:tmp] + _ex[tmp + 2:]

        # print('_ex', _ex, _ex[-1])
        a.append(abs(int(_ex[-1])))

    return max(a)


print(solution_other(expression="100-200*300-500+20"))
