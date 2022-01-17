# (11) 수식의 괄호 검사 (스택)


class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


# 소괄호: ( )
# 중괄호: { }
# 대괄호: [ ]
# 포함할 수 있는 수식을 표현한 문자열 expr 이 인자로 주어질 때, 이 수식의 괄호가 올바르게 여닫혀 있는지를 판단하는 함수
def solution(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    S = ArrayStack()
    for c in expr:
        if c in '({[':
            # 열린괄호를 만나면
            S.push(c)
        elif c in match:
            # 닫힌괄호를 만나면
            if S.isEmpty():
                return False
            else:
                t = S.pop()
                # 짝이 맞으면
                if t != match[c]:
                    return False

    return S.isEmpty()


# TEST
temp = '({[]})'

match = {
        ')': '(',
        '}': '{',
        ']': '['
    }

for c in temp:
    if c in '({[':
        print(f'open :: {c}')
    if c in 'a+b':
        print(f'item :: {c}')
    elif c in match:
        print(f'close :: {c}, {match[c]}')
# TEST

print(solution('{[()]'))