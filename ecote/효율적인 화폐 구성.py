# 다이나믹 프로그래밍
# N가지 종류의 화폐가 있다.
# 이 화폐들의 개수를 최소한으로 이용해 합이 M원이 되도록 만들기

# 첫째 줄에 M이 주어진다. (1 <= M <= 10,000)
# N개의 각 화폐의 가치는 1이상 10,000보다 작거나 같은 자연수

def solution(m, moneys):
    # 각 화폐(k)를 순서대로 확인하면서
    # k로 만들 수 있는 개수를 넣고,
    # 이미 값이 있으면 최솟값을 이용한다.
    # a[i] = a[i-k] + 1
    # a[i] = min(a[i], a[i-k] + 1)
    n = len(moneys)
    d = [10001] * (m + 1)

    d[0] = 0
    for i in range(n):
        for j in range(moneys[i], m + 1):
            d[j] = min(d[j], d[j - moneys[i]] + 1)

    return -1 if d[m] == 10001 else d[m]


print(solution(m=15, moneys=[2, 3]))
