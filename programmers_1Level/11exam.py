# 제일 작은 수 제거하기

def minPop(arr):
    min = arr[0]
    for k in arr:
        if k < min:
            min = k

    del arr[arr.index(min)]
    return arr or [-1]


print(minPop([4, 5, 3, 2, 1]))
print()


# 다른 사람의 풀이
# min 함수 사용하면 느려서 시간초과된다. 사용금지

def solution(arr):
    result = [k for k in arr if k > min(arr)]
    print(result or [-1])


solution([4])
