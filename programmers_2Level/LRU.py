# [1차] 캐시

# 해당 값이 캐시 안에 있으면 해당 값을 캐시의 최근 위치에 넣고,
# 해당 값이 캐시 안에 없으면 가장 오래 전에 참조된 값을 제거하고 최근 위치에 넣어준다.
# 캐시 사이즈를 확인해서 넣어준다.

def solution(cacheSize, cities):
    answer = 0
    cache = []
    for ref in cities:
        ref = ref.lower()
        if not ref in cache:
            if len(cache) < cacheSize:
                cache.append(ref)
            else:
                if cache:
                    cache.pop(0)
                    cache.append(ref)
            answer += 5
        else:
            cache.pop(cache.index(ref))
            cache.append(ref)
            answer += 1
    return answer


# print(solution(cacheSize=3,
#                cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# print(solution(cacheSize=3,
#                cities=["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
# print(solution(cacheSize=3,
#                cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# print(solution(cacheSize=5,
#                cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# print(solution(cacheSize=2,
#                cities=["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(cacheSize=0,
               cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))


# 다른 사람의 풀이
# 큐에 maxlen을 주게 되면 해당 사이즈가 넘어서면 자동으로 pop(0) 진행되고 append() 된다.

def solution_other(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
