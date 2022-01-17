# 영어 끝말잇기
# 단어를 중복해서 말하는 경우, 다른 단어로 말하는 경우 탈락


from collections import defaultdict


def solution(n, words):
    end = ''
    dic = defaultdict(int)
    for index, word in enumerate(words):
        if not end:
            end = word[-1]
            dic[word] += 1
        else:
            if dic.get(word, 0) > 0 or word[:1] != end:
                # print(index, word, "이미 사용된 단어이거나 끝단어와 맞지 않습니다.",
                #       (index % n) + 1, '번째 사람이', (index // n) + 1, '차례에 말을 할때 탈락했습니다.' )
                return [(index % n) + 1, (index // n) + 1]
            else:
                dic[word] += 1
                end = word[-1]

    return [0, 0]


# print(solution(n=3, words=["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# print(solution(n=5,
#                words=["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish",
#                       "hang", "gather", "refer", "reference", "estimate", "executive"]))
# print(solution(n=2, words=["hello", "one", "even", "never", "now", "world", "draw"]))


# 다른 사람의 풀이

def solution_other(n, words):
    for p in range(1, len(words)):
        if words[p - 1][-1] != words[p][0] or words[p] in words[:p]:
            return [(p % n) + 1, (p // n) + 1]
    else:
        return [0, 0]


print(solution_other(n=3, words=["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
