from collections import defaultdict


def solution(gems):
    n = len(gems)
    answer = []
    kind = len(set(gems))
    count = n

    # 2중 for문 효율성 터진다.
    # for i in range(n - len(s) + 1):
    #     for j in range(i + len(s) - 1, n):
    #         if set(gems[i:j + 1]).issuperset(s):
    #             answer.append([i + 1, j + 1])
    #
    # answer.sort(key=lambda x: x[1] - x[0])

    check_set = defaultdict(int)
    start = end = 0
    while end < n:
        check_set[gems[end]] += 1
        end += 1

        # dict 개수를 카운트하고 끝점을 증가시킨다.
        # 종류 개수가 일치하게 되면 시작점을 증가시켜서 최소가 되는 길이를 찾는다.
        if kind == len(check_set):
            while start < end:
                if check_set[gems[start]] > 1:  # 최소 1개를 보유해야함
                    check_set[gems[start]] -= 1
                    start += 1
                elif end - start - 1 < count:
                    count = end - start - 1
                    answer = [start + 1, end]
                    break
                else:
                    break

    return answer


print(solution(gems=["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(gems=["AA", "AB", "AC", "AA", "AC"]))
print(solution(gems=["XYZ", "XYZ", "XYZ"]))
