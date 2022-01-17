# 괄호 회전하기

def solution(s):
    answer = 0
    l = len(s)

    if l % 2 != 0:
        return answer

    def check(s):
        nList = []
        stack = []

        count = 0
        dic = {']': '[',
               '}': '{',
               ')': '('}
        for i in s:
            if i in ('[', '(', '{'):
                stack.append(i)
            else:
                print(f'닫힌 괄호다. stack={stack}')
                # 닫힌 괄호다.
                if stack:
                    end = stack[-1]
                    print(f'스택 끝={end}, 현재값={i}')
                    if dic[i] == end:
                        stack.pop()
                        count += 2
                        if not stack:
                            nList.append(count)
                            count = 0
                    else:
                        return []
                else:
                    return []

        return nList

    for i in range(l):
        if i:
            s = s[1:] + s[:1]

        li = check(s=s)
        print('x=', i, s, 'li=', li)
        if li:
            answer += 1

    return answer


print(solution(s="([{)}]"))

