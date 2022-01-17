# 모험가 길드

def solution(n, gong):
    answer = 0
    # 공포도가 낮은 순으로 정렬
    gong.sort()

    dic = {}
    for g in gong:
        if not dic.get(g, 0):
            dic[g] = g
        dic[g] -= 1

        if dic.get(g, 0) == 0:
            answer += 1

    return answer


print(solution(n=5, gong=[2, 3, 1, 2, 2]))


def other_solution(n, data):
    data.sort()

    result = 0  # 총 그룹의 수
    count = 0  # 현재 그룹에 포함된 모험가의 수

    for i in data:
        count += 1  # 현재 그룹에 해당 모험가를 포함시키기 
        if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이면 그룹으로 결성
            result += 1  # 그룹 수 증가
            count = 0  # 현재 그룹에 포함된 모험가 수 초기화

    return result
