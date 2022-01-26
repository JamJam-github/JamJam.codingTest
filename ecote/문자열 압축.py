# step 1 ~ n / 2까지 반복해서 최소 길이가 되는 구간

def solution(s):
    n = len(s)
    answer = n

    for i in range(1, n // 2 + 1):
        compressed = ''  # i개 단위로 압축한 문자열
        prev = s[0:i]
        count = 1
        for j in range(i, n, i):  # i개 단위로 증가하며 비교
            if prev == s[j:j + i]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + i]
                count = 1

        # i개 단위로 압축한 문자열 끝에 남아있는 것
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer


print(solution(s="aabbaccc"))
print(solution(s="ababcdcdababcdcd"))
print(solution(s="abcabcdede"))
print(solution(s="aaaabbabbabb"))
