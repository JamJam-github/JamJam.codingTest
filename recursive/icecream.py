# 음료수 얼려 먹기
# N * M 크기의 얼음 틀이 있습니다.
# 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결된 것으로 간주한다.
# 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하시오.
# 4 * 5 얼음 틀에서는 아이스크림이 총 3개 생성됩니다.

graph = [[0, 0, 1, 1, 0],
         [0, 0, 0, 1, 1],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0]]

n, m = 4, 5


def dfs(i, j):
    # 주어진 범위를 벗어나는 경우
    if i < 0 or i >= n or j < 0 or j >= m:
        return False

    if graph[i][j] == 0:
        graph[i][j] = 1
        # 상하좌우 재귀호출
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
        dfs(i + 1, j)
        return True
    return False


def icecream_dfs(n, m):
    result = 0
    for i in range(n):
        for j in range(m):
            # 처음 방문할때만 True가 나올 것이다. dfs 내부에서 연결된 노드들을 모두 방문처리해놔서
            if dfs(i, j) == True:
                result += 1

    return result


print(icecream_dfs(n, m))
