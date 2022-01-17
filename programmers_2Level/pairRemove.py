# 짝지어 제거하기

def solution(s):
    stack = []
    for idx, text in enumerate(s):
        if stack:
            if stack[-1] == text:
                stack.pop()
            else:
                stack.append(text)
        else:
            stack.append(text)

    if stack:
        return 0
    return 1


print(solution(s="cdcd"))
