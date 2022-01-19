# 서로소 집합 알고리즘
# 학생들은 0 ~ N번까지의 번호를 부여했다.
# 처음에는 모든 학생이 서로 다른팀으로 구분되어 총 N+1개 팀이 존재한다.
# '팀 합치기' 연산은 0 a b 형태로 주어진다.
# '같은 팀 여부 확인' 연산은 1 a b 형태로 주어진다.

# 루트 노드를 찾을 때까지 재귀적으로 호출
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 찾고 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 더 작은 값이 부모노드
    # 같은 값인 경우 사이클이 발생한 것이다.
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, m, array):
    parent = [i for i in range(n + 1)]
    # print(parent)

    for i in range(m):
        oper, a, b = array[i]
        if oper:
            if find_parent(parent, a) == find_parent(parent, b):
                print('YES')
            else:
                print('NO')
        else:
            union_parent(parent, a, b)

    return ''


print(
    solution(n=7, m=8,
             array=[[0, 1, 3], [1, 1, 7], [0, 7, 6], [1, 7, 1], [0, 3, 7], [0, 4, 2], [0, 1, 1], [1, 1, 1]]))
