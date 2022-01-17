# 문자열 다루기 기본

def solution(s):
    answer = True
    if not len(s) in (4, 6):
        return False

    for i in s:
        if 48 <= ord(i) <= 57:
            pass
        else:
            return False

    return True


# 다른 사람의 풀이
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)


# -----------------------
# 문자열 내림차순으로 배치하기
# A-Z 65-90, a-z 97-122
# sorted 함수는 문자열도 정리해주기 때문에 아스키코드가 필요없다.

s = "Zbcdefg"
# l = sorted([ord(k) for k in s], reverse=True)
# u = sorted([ord(k) for k in s if 65 <= ord(k) <= 90])
print(''.join(sorted(s, reverse=True)))
print()

# -------------------
# 문자열 내 p와 y의 개수
# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다.
# s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요.

s = "pPoooyY"


def solution(s):
    return s.lower().count('p') == s.lower().count('y')


print(solution(s))
print()

# 문자열 내 마음대로 정렬하기
strings, n = ["abce", "abcd", "cdx"], 2

array = sorted(strings, key=lambda x: (x[n], x))
print('각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하기:')
print(array)

