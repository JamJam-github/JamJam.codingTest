# 다음 큰 숫자

def solution(n):
    one = format(n, 'b').count('1')
    for i in range(n+1, 1000001):
        if bin(i).count('1') == one:
            return i


print(solution(n=78))
