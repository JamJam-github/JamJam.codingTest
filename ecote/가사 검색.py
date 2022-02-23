from collections import defaultdict
from bisect import bisect_left, bisect_right


# 'fro??' 인 경우 'froaa' 인덱스와 'frozz' 인덱스를 리턴한다.
def count_by_range(data, x):
    start = bisect_left(data, x.replace('?', 'a'))
    end = bisect_right(data, x.replace('?', 'z'))
    return end - start


def solution(words, queries):
    answer = []
    data, revered_data = defaultdict(list), defaultdict(list)
    for word in words:
        data[len(word)].append(word)
        # 접두사 와일드 카드는 뒤집은 채 검사하기
        revered_data[len(word)].append(word[::-1])

    # print(data)
    # print(revered_data)
    for k, v in data.items():
        data[k].sort()
    for k, v in revered_data.items():
        revered_data[k].sort()
    print('정렬 후', data)
    print('정렬 후', revered_data)

    for query in queries:
        length = len(query)
        # 접두사가 와일드 카드인 경우 '????o' -> 'oaaaa' ~ 'ozzzz' 찾기
        if query[0] == '?':
            count = count_by_range(revered_data[length], query)
        else:
            count = count_by_range(data[length], query)

        answer.append(count)
    return answer


print(solution(words=["frodo", "front", "frost", "frozen", "frame", "kakao"],
               queries=["fro??", "????o", "fr???", "fro???", "pro?"]))
