# DFS

num = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9


def dfs(i, now):  # 위치, 현재 값
    global min_value, max_value, add, sub, mul, div

    if i == num:  # 모든 연산자를 사용했을 때
        min_value = min(min_value, now)
        max_value = max(max_value, now)
        return
    else:
        if add > 0:
            add -= 1  # + 수 차감
            dfs(i + 1, now + data[i])  # 연산자를 모두 사용했을 때 나옴
            add += 1  # + 복구, 위에서 나온 뒤 sub로 내려감
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1


dfs(1, data[0])

print(max_value)
print(min_value)
