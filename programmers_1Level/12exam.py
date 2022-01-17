# 정수 제곱근 판별

n = 100


def solution1(n):
    root = n ** 0.5
    if root == int(root):
        return (root + 1) ** 2
    return -1


# 정수 내림차순으로 배치하기
n = 118372


def solution2(n):
    new = sorted(list(str(n)), reverse=True)
    print(int(''.join(new)))


# 자연수 뒤집어 배열로 만들기
# arr[A:B:C]는 index A 부터 index B 까지 C의 간격으로 배열을 만들라는 의미임.
n = 12345


def solution3(n):
    nList = list(map(int, str(n)[::-1]))
    print(nList)


# 자릿수 더하기
# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
n = 987


def solution4(n):
    nList = list(map(int, str(n)))
    sum = 0
    for i in nList:
        sum += i
    print(sum)


# 다른 사람의 풀이
# n % 10 나머지를 더하고, 재귀함수로 n // 10 전달하기
# return (n % 10) + sum_digit(n // 10)


# 이상한 문자 만들기
s = "tryyyyyyyyyyyyy helloooooooooooooooooo worldddddddddddddddddddd"
answer = []
for i in s.split(' '):
    tmp = ""
    for idx, j in enumerate(i):
        if idx % 2 == 0:
            tmp += j.upper()
        else:
            tmp += j.lower()
    answer.append(tmp)

print(' '.join(answer))


# 다른 사람의 풀이
# 람다식으로 표현
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

