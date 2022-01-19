# 그리디 알고리즘
# N개의 동전을 이용하여 만들 수 없는 양의 정수 중 최솟값

def solution(n, coins):
    # 화폐 단위를 정렬하고 작은 단위부터 확인하기
    # 누적합보다 화폐가 큰 경우 그 사이에 갭이 생겼다는 의미.
    coins.sort()
    target = 1
    for x in coins:
        if target < x:
            break
        target += x

    return target


print(solution(n=5, coins=[3, 2, 1, 1, 9]))
