# [3차] n진수 게임

# 숫자를 0부터 시작해서 차례대로 말한다.
# 첫 번째 사람은 0, 두 번째 사람은 1, … 열 번째 사람은 9를 말한다.
# 10 이상의 숫자부터는 한 자리씩 끊어서 말한다.

# format(10, 'b') 'b'는 2진법, 'o'는 8진법, 'x'는 16진법

def solution(n, t, m, p):
    answer = ''

    # 10진수 -> N진수 변경
    def convert(num, base):
        temp = "0123456789ABCDEF"
        q, r = divmod(num, base)

        if q == 0:
            return temp[r]
        else:
            # q를 base로 변환
            # 즉, n진수의 다음 자리를 구함
            return convert(q, base) + temp[r]

    baseN = ''
    for i in range(t * m):
        baseN += convert(i, n)

    # length = len(baseN)
    # count = 0
    # for i in range(p - 1, length, m):
    #     answer += baseN[i:i + 1]
    #     count += 1
    #
    #     if count == t:
    #         break
    while len(answer) < t:
        answer += baseN[p - 1]
        p += m

    return answer


print(solution(n=2, t=4, m=2, p=1))
print(solution(n=16, t=16, m=2, p=1))
print(solution(n=16, t=16, m=2, p=2))
