# 뉴스 클러스터링
# 다중집합은 중복을 허용하는 set과 다른 개념

# 두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 "교집합 크기 / 합집합 크기" 정의된다.
# A = {1, 2, 3}, 집합 B = {2, 3, 4}라고 할 때,
# 교집합 A ∩ B = {2, 3}, 합집합 A ∪ B = {1, 2, 3, 4}이 되므로,
# 집합 A, B 사이의 자카드 유사도 J(A, B) = 2/4 = 0.5

# 다중집합 A는 원소 "1"을 3개 가지고 있고, 다중집합 B는 원소 "1"을 5개 가지고 있다고 하자.
# 이 다중집합의 교집합 A ∩ B는 원소 "1"을 min(3, 5)인 3개, 합집합 A ∪ B는 원소 "1"을 max(3, 5)인 5개 가지게 된다.
# 다중집합 A = {1, 1, 2, 2, 3}, 다중집합 B = {1, 2, 2, 4, 5}라고 하면,
# 교집합 A ∩ B = {1, 2, 2}, 합집합 A ∪ B = {1, 1, 2, 2, 3, 4, 5}가 되므로,
# 자카드 유사도 J(A, B) = 3/7, 약 0.42가 된다.

# 문자열 "FRANCE"와 "FRENCH"가 주어졌을 때, 이를 두 글자씩 끊어서 다중집합을 만들 수 있다.
# 각각 {FR, RA, AN, NC, CE}, {FR, RE, EN, NC, CH}가 되며,
# 교집합은 {FR, NC}, 합집합은 {FR, RA, AN, NC, CE, RE, EN, CH}가 되므로,
# 두 문자열 사이의 자카드 유사도 J("FRANCE", "FRENCH") = 2/8 = 0.25가 된다.


def solution(str1, str2):
    # 두 글자씩 끊어서 다중집합의 원소로 만든다.
    # 특수문자가 있는 경우 글자 쌍을 버린다.
    # ->> 대소문자 구분없이 같은 것으로 여기니까 lower로 원소 만들자.
    a, b = [], []
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            a.append(str1[i:i + 2].lower())

    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            b.append(str2[i:i + 2].lower())

    a_temp, b_temp, inter = a.copy(), b.copy(), []
    for i in a:
        if i in b_temp:
            inter.append(i)
            b_temp.remove(i)
            a_temp.remove(i)

    union = inter + a_temp + b_temp

    if not inter and not union:
        return 65536

    return int(65536 * (len(inter) / len(union)))


print(solution(str1="FRANCE", str2="french"))
print(solution(str1="handshake", str2="shake hands"))
print(solution(str1="aa1+aa2", str2="AAAA12"))
print(solution(str1="E=M*C^2", str2="e=m*c^2"))


# 다른 사람의 풀이

import re
def solution_other(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0:
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return int(65536 * (gyo_sum/hap_sum))