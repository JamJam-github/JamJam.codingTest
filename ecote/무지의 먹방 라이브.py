# 그리드 문제


def solution(food_times, k):
    n = len(food_times)

    foods = []
    for i in range(n):
        foods.append((food_times[i], i + 1))
    foods.sort()

    pretime = 0  # 직전에 소요한 시간
    for i, food in enumerate(foods):
        diff = food[0] - pretime  # 높이 = 음식 시간 - 직전에 소요한 시간
        if diff != 0:
            spend = diff * n  # 높이 * 남은 음식
            if spend <= k:
                k -= spend
                pretime = food[0]
            else:
                k %= n
                sublist = sorted(foods[i:], key=lambda x: x[1])
                # 남은 음식의 번호 순으로 정렬시키고 나머지 음식의 번호
                return sublist[k][1]

        n -= 1

    return -1


print(solution(food_times=[3, 1, 2], k=5))
print(solution(food_times=[3, 5, 1, 6, 5, 3], k=20))
