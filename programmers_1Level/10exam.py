# 최대공약수와 최소공배수

def solution(n, m):
    answer = []

    # 최대 공배수
    # n, m 중 작은 숫자부터 1까지 for 반복.
    # 나머지가 없는 상태의 경우 i가 n, m의 최대 공약수이다. (n, m을 모두 나눌 수 있는 약수 중 가장 큰 수)
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break

    # 최소 공배수
    # n, m 중 큰 숫자부터 n*m까지 for 반복.
    for i in range(max(n, m), n * m + 1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break

    return answer


# print(solution(3, 12))
# print(solution(2, 5))
# print(solution(1071, 1029))
print()


# 다른 사람의 풀이
# 유클리드 호제법 : 두 수가 서로 상대방 수를 나누어 결국 원하는 수를 얻는 알고리즘.
# 1) 최대 공약수: (a > b) a를 b로 나눈 나머지 r 이라 하면, a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
# b를 r로 나눈 나머지 r' 구하고, r를 r'로 나눈 나머지 r" ... (반복)
# 나머지 r가 0이 되도록 나눠지는 수가 a와 b의 최대공약수가 된다.
# 2) 최소 공배수: a * b를 최대공약수로 나눈 몫.

def gcd(a, b):
    return gcd(b, a % b) if b else a


def lcm(a, b):
    result = a * b // gcd(a, b)
    return result


# print(gcd(1071, 1029))
# print(lcm(1071, 1029))
print(lcm(2, 6))
print(lcm(6, 8))
print(lcm(24, 14))

# math 내에 gcd, lcm이 존재한다.
# math.lcm(24, 14) 혹은 math.gcd(6, 8)