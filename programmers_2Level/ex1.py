# 괄호 변환


def solution(p):
    # 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. (열린/닫힌 괄호 개수만 맞으면 균형 문자열이다)
    def divide(p):
        openCnt, cloCnt = 0, 0
        for i in range(len(p)):
            if p[i] == '(':
                openCnt += 1
            else:
                cloCnt += 1
            if openCnt == cloCnt:
                return p[:i + 1], p[i + 1:]

    def separate(w):
        # 1단계
        if not w:
            return ''

        # 2단계
        u, v = divide(p=w)
        print(f'2단계:: u = {u}, v = {v}')

        # 3단계
        stack = []
        for text in u:
            if stack:
                if text == ')':
                    stack.pop()
                else:
                    stack.append(text)
            else:
                stack.append(text)
        print('3단계::', u, '->', stack)

        # 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
        if not stack:
            print(f'올바른 괄호 문자열 {u}, 재수행할 {v} ')
            answer = u + separate(v)
            return answer
        # 문자열 u가 "올바른 괄호 문자열"이 아니라면 4단계를 수행하여 반환합니다.
        else:
            answer = '('
            answer += separate(v)
            answer += ')'
            # answer += (u[1:-1])[::-1]
            for st in u[1:-1]:
                if st == '(':
                    answer += ')'
                else:
                    answer += '('
            return answer

    return separate(w=p)


print(solution(p="(()())()"))
# print(solution(p=")("))
# print(solution(p="()))((()"))
