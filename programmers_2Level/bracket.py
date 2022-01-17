# 올바른 괄호
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때,
# 문자열 s가 올바른 괄호이면 true를 return 하고,
# 올바르지 않은 괄호이면 false를 return 하는 solution 함수


def solution(s):
    stack = []
    for text in s:
        if not stack:
            stack.append(text)
        else:
            if text == '(':
                stack.append(text)
            else:
                if stack[-1] == '(':
                    stack.pop()

    return len(stack) == 0


print(solution(s="(())()"))
print(solution(s=")()("))
print(solution(s="(()("))


# 최댓값과 최솟값

def solution2(s):
    sl = list(map(int, s.split(' ')))
    return '{0} {1}'.format(min(sl), max(sl))

print(solution2(s="1 2 3 4"))
print(solution2(s="-1 -2 -3 -4"))
print(solution2(s="-1 -1"))
