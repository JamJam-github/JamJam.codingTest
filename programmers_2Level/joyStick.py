# 조이스틱

from collections import defaultdict

def solution(name):
    answer = 0
    # alpha = [chr(i) for i in range(65, 91)]
    # print(alpha)

    # 문자열에 대한 가중치를 구해놓기
    # [A, B, C, D... N ... Z] 총 26개의 중간은 13번째 'N'
    # 중간 'N'을 기준으로 왼쪽은 가중치가 증가하고 오른쪽은 가중치가 감소한다.
    # [0, 1, 2, 3, ... , 12, 13, 12, 11, 10, ... 3, 2, 1, 0]
    counter = [min(ord(i) - ord('A'), ord('Z') - ord(i)+1) for i in name]
    print(name, '가중치 ::', counter, '총 가중치 :: ', sum(counter))

    # 가장 긴 A를 구하자.
    aMax, cnt = -float('inf'), 0
    for i in name:
        if i == 'A':
            cnt += 1
            aMax = max(aMax, cnt)
        else:
            cnt = 0

    if 'A' in name:
        print(f'전체 길이 :: {len(name)}, 가장 긴 A length:: {aMax}, A의 인덱스 {name.index("A"*aMax)}')
        index = name.index("A" * aMax) if aMax else 0
        if aMax > index:
            return sum(counter) + ((index - 1) * 2) + (len(name) - aMax - index) + 1
        else:
            return sum(counter) + len(name) - 1




    # idx = 0
    # dic = defaultdict(int)
    # for i in range(65, 78):
    #     idx += 1
    #     dic[chr(i)] = idx
    # for i in range(78, 91):
    #     idx -= 1
    #     dic[chr(i)] = idx
    #
    # print(dic)
    #
    # length = len(name)
    # index = 0
    # for n in name:
    #     diff = ord(n) - ord('A')
    #     print('이름::', n, 'dif=', diff, 'dic=', (dic[n]+1))
    #     index += 1
    #     if index < length:
    #         answer += 1
    #
    #     if diff < 13:
    #         answer += diff
    #     else:
    #         # answer += 1
    #         answer += (dic[n] + 1)


    return sum(counter) + len(name) - 1

# print(solution(name="AABAAAAAAABB"))
print(solution(name="JAZ"))
# print(solution(name="JAN"))
# print(solution(name="JEROEN"))