# 폰켓몬

def solution(nums):
    l = len(nums) // 2
    answer = len(list(set(nums))[:l])
    return answer


print(solution(nums=[3, 1, 2, 3]))

# 다른 사람의 풀이
# min(len(ls)/2, len(set(ls)))
# N/2와 중복제거한 길이 중에서 작은 것을 택하면 된다.
