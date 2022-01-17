# 모음 사전

# 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는 단어
# A -> AA -> AAA -> AAAA -> AAAAA -> AAAAE -> AAAAI -> AAAAO -> AAAAU ->
# AAAE -> AAAI...
def solution(word):
    answer = 0
    length = len(word)
    dic = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}

    # 첫번째 자리에서 A의 개수
    result = 0
    if word[:1] == 'A':
        for i in range(len(word)):
            if word[i] == 'A':
                result += 1
            else:
                break

    word = word[result:]
    print(f'현재 word = {word}, result = {result}, 남은 자리 수 = {len(word)}')

    # for i in range(len(word)):


    return result


print(solution(word="AAAAE"))