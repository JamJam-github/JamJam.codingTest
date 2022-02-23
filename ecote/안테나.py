# 안테나는 집이 위치한 곳에만 설치할 수 있다.

# 정확히 중간값에 해당하는 위치에 안테나를 설치했을 때
# 총합이 최소가 된다.

def solution(data):
    n = len(data)
    data.sort()
    # min_value = float('inf')
    # for i in range(len(data)):
    #     total = 0
    #     for j in range(len(data)):
    #         total += abs(data[i] - data[j])
    #     min_value = min(min_value, total)

    return data[(n-1) // 2]


print(solution(data=[5, 1, 7, 9]))