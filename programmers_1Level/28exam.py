answer = 0
friends = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'}

def dfs(names, isVisited, data):
    return 1


def solution(n, data):
    isVisited = [False] * 8
    print(isVisited)

    dfs("", isVisited, data)
    return answer


print(solution(n=2, data=["N~F=0", "R~T>2"]))
