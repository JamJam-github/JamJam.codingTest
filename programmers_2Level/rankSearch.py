# 순위 검색

# info = "개발언어 직군 경력 소울푸드 점수"
# query = "개발언어 and 직군 and 경력 and 소울푸드 [숫자 점수]"
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    answer = []
    info = [i.split(' ') for i in info]
    dic = defaultdict(list)

    for i in info:
        # tmp = '{0}-{1}-{2}-{3}'.format(i[0], i[1], i[2], i[3])
        # 0자리 부터 4자리까지 조합
        for j in range(5):
            for com in combinations(i[:-1], j):
                # print('com::', com, type(com))
                tmp = ''.join(com)
                dic[tmp].append(int(i[4]))
                # print(''.join(com))
                # print(dic)
        # dic[tmp].append(i[4])
    print('dic=', dic)
    for name in dic:
        dic[name].sort()

    # print('정렬 후 dic::', dic)

    for i in query:
        find = i.replace(' and ', '').replace('-', '').split(' ')
        print('query=', find, 'score=', dic[find[0]])

        if find[0] in dic:
            # scores = 쿼리 매칭 점수 dic[find[0]]
            # 구하려는 기준 점수 = int(find[1])
            # bisect_left :: 정렬 후 이분탐색, 정렬된 list에 x를 삽입할 위치를 리턴해준다.
            result = bisect_left(dic[find[0]], int(find[1]))
            answer.append(len(dic[find[0]]) - result)
        else:
            answer.append(0)

        # for f in dic[find[0]]:
        #     if int(find[1]) <= int(f):
        #         count += 1
        # print(f'현재 {f}는 기준 {find[1]} 이상에 해당된다.')

    return answer


print(solution(
    info=["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
          "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    query=["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
           "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
           "- and - and - and - 150"]))



# 다른 사람의 풀이

def solution_other(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
        answer.append(len(pool)-l)

    return answer