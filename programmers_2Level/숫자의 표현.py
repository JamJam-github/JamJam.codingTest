

def solution(n):
    answer = 0

    for i in range(1, n+1):
        result = 0
        for j in range(i, n+1):
            result += j
            print(j, ' ', end='')
            if result == n:
                answer += 1
                break

            if n < result:
                break

        print()
    return answer


print(solution(n=15))