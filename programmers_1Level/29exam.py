# 124 나라의 숫자
# 124 나라에는 10진법이 아닌 1, 2, 4만 사용합니다.

# 3진법으로 표현할때 0으로 나누어 떨어질 경우 몫-1, 나머지 0인 경우 4로 치환.

def solution(n):
    answer = ''
    while n > 0:
        n, rest = divmod(n, 3)
        if rest == 0:
            n -= 1
        answer += '4' if rest == 0 else str(rest)
    return answer[::-1]


print(solution(n=4))