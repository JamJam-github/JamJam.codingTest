

def solution(triangle):
    n = len(triangle)

    # DFS 효율성 터진다.
    # answer = 0
    # queue = deque()
    # queue.append((0, 0, triangle[0][0]))
    #
    # while queue:
    #     i, j, value = queue.popleft()
    #
    #     if i == (n - 1):
    #         answer = max(answer, value)
    #         continue
    #     else:
    #         i += 1
    #         queue.append((i, j, value + triangle[i][j]))
    #         queue.append((i, j + 1, value + triangle[i][j + 1]))

    d = [[0 for _ in range(1, _ + 1)] for _ in range(1, n + 1)]
    d[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                d[i][j] = triangle[i][j] + d[i - 1][j]
            elif i == j:
                d[i][j] = triangle[i][j] + d[i - 1][j - 1]
            else:
                d[i][j] = triangle[i][j] + max(d[i-1][j-1], d[i-1][j])

    return max(d[-1])


print(solution(triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
