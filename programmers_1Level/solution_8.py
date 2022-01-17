# Level 1) 하샤드 수

def solution(x):
    n, sum = int(x), 0
    while n > 0:
        sum += n % 10
        n //= 10

    return int(x) % sum == 0


x = "12"
print(solution(x))
print()

# 다른 사람의 풀이
# 리스트의 sum을 사용할 수 있다.

sum = sum([int(c) for c in str(x)])
print(int(x) % sum == 0)
