# 순열: 서로 다른 n개의 원소에서 r개를 중복없이 골라 순서대로 나열하는 경우의 수
# 조합: 서로 다른 n개의 원소에서 r개를 뽑는 경우의 수

# 재귀를 이용한 순열 구현
# 원소를 하나씩 뽑아서 수열을 구성하고 출력
# 8개 모든 가능한 순열은 8!=40320개

def permutation(arr, r):
    # arr = sorted(arr)
    visited = [False] * len(arr)

    def generate(chosen, visited):
        if len(chosen) == r:
            print(chosen)
            return

        for i in range(len(arr)):
            if not visited[i]:
                chosen.append(arr[i])
                visited[i] = True
                generate(chosen, visited)
                visited[i] = False
                chosen.pop()

    generate([], visited)


print(permutation(arr=['A', 'B', 'C', 'D'], r=4))


# 제너레이터를 이용한 구현
# 한 원소를 뽑고 그 원소를 제외한 나머지 배열로 다시 함수를 호출
def permutations_2(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in permutations_2(arr[:i] + arr[i + 1:], r - 1):
                yield [arr[i]] + next


# print(permutations_2(arr=['A', 'B', 'C', 'D'], r=4))


# 조합
# 제너레이터를 이용한 구현
def combinations_2(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations_2(arr[i+1:], r-1):
                yield [arr[i]] + next


# print(combinations_2(arr=['A', 'B', 'C', 'D'], r=4))