# (13) 후위표현 수식 계산

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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


# 중위표현식을 후위표현식으로 바꾸는 함수
def infixToPostfix(tokenList):
    prec = {
        '*': 3, '/': 3,
        '+': 2, '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for t in tokenList:

        if type(t) is int:
            postfixList.append(t)
        else:
            if opStack.isEmpty():
                opStack.push(t)
            elif t == '(':
                opStack.push(t)
            elif t == ")":
                while opStack.peek() != "(":
                    postfixList.append(opStack.pop())
                opStack.pop()
            elif t in "*+/-":
                while prec[opStack.peek()] >= prec[t]:
                    postfixList.append(opStack.pop())
                    if opStack.isEmpty():
                        break
                opStack.push(t)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


# 후위표현식을 연산하는 함수
def postfixEval(tokenList):
    opStack = ArrayStack()
    val = 0

    for t in tokenList:
        if type(t) is int:
            opStack.push(t)
        else:
            a = opStack.pop()
            b = opStack.pop()
            if t == "*":
                opStack.push(a * b)
            elif t == "/":
                opStack.push(b / a)
            elif t == "+":
                opStack.push(a + b)
            else:
                opStack.push(b - a)

    if not opStack.isEmpty():
        val = opStack.peek()

    return val


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val


# tokens = splitTokens("(1+2)*(3+4)")
# print(f'token :: {tokens}')
# postfix = infixToPostfix(tokens)
# print(f'postfix :: {postfix}')
# val = postfixEval(postfix)
# print(f'val :: {val}')

