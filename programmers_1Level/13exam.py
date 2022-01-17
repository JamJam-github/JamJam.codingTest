# 약수의 합

n = 12


def solution(n):
    return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])


# print(solution(n))


# 시저 암호

def solution2(s, n):
    for num in range(n):
        new_s = ''
        for i in s:
            o = ord(i)

            if o == 32:
                new_s += i
            elif o == 122:
                new_s += 'a'
            elif o == 90:
                new_s += 'A'
            else:
                new_s += chr(o + 1)
        s = new_s

    return s


print(solution2("a B z", 4))

# 다른 사람의 풀이
# 1) 알파벳 여부로 분리
# 2) 대소문자 여부로 분리 (a-z, A-Z 항상 26차이가 발생한다)
# 3) result += chr((ord(i) - ord("a") + n) % 26 + ord("a"))
#    result += chr((ord(i) - ord("A") + n) % 26 + ord("A"))
