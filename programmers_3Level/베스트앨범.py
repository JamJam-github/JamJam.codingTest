# 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다.
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

from collections import defaultdict


def solution(genres, plays):
    answer = []

    dic = defaultdict(int)  # 장르별 재생횟수
    dic2 = defaultdict(list)  # {key 장르: value (고유번호, 재생횟수)}
    for i in range(len(genres)):
        dic[genres[i]] += plays[i]
        dic2[genres[i]].append((i, plays[i]))

    print('dic', dic)
    print('dic2', dic2)
    
    # 딕셔너리 정렬
    dic_items = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print('dic.items()', dic.items())
    print('dic_items', dic_items)

    for key, value in dic_items:
        dic2_items = sorted(dic2[key], key=lambda x: x[1], reverse=True)
        # print('dic2_items', dic2_items)
        for d2 in dic2_items[:2]:
            answer.append(d2[0])

    return answer


print(solution(genres=["classic", "pop", "classic", "classic", "pop"],
               plays=[500, 600, 150, 800, 2500]))
