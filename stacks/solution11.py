# (12) 중위표현 수식 --> 후위표현 수식


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


# 연산자의 우선순위
prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


# A - Z 까지와 4칙연산을 나타내는 연산자 기호 +, -, *, /, 그리고 여는 괄호와 닫는 괄호 (, ) 로 이루짐
def solution(S):
    opStack = ArrayStack()
    answer = ''

    for c in S:
        # 피연산자의 경우
        if c not in "*+-/()":
            answer += c
        else:
            if opStack.isEmpty():
                opStack.push(c)
            # 열린 괄호는 항상
            elif c == "(":
                opStack.push(c)
            # 닫힌 괄호면 열린괄호가 나올때까지 순회
            elif c == ")":
                while opStack.peek() != "(":
                    answer += opStack.pop()
                opStack.pop()
            # 괄호를 제외한 연산자의 경우
            elif c in "*+/-":
                # 기존 연산자의 우선순위가 큰 경우
                while prec[opStack.peek()] >= prec[c]:
                    answer += opStack.pop()
                    if opStack.isEmpty():
                        break
                opStack.push(c)

    # 스택에 남은 데이터 처리
    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer


print(solution('(A+(B-C))*D'))
print("############################")
print(solution('A*B+C'))
print("############################")
print(solution('A+B*C'))
print("############################")
print(solution('A+B+C'))