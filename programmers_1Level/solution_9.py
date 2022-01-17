# Level 1) 콜라츠 추측


def solution(n):
    cnt = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        cnt += 1

        if cnt >= 500:
            return -1

    return cnt


print(solution(6))


# 다른 사람의 풀이
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        if num == 1:
            return i + 1
    return -1
