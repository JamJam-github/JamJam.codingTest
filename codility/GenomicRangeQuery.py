# A , C , G 및 T 유형의 뉴클레오티드는 각각 1, 2, 3 및 4의 영향 계수를 갖습니다.
# 문자열 S 에서 P[i] ~ Q[i] 번째 문자열 중에서
# 최소 영향인자를 구하기

# min() 사용시 O(N * M)
# O(N + M)으로 해결해야 한다.

def solution(S, P, Q):
    answer = []
    # dict = {"A": 1, "C": 2, "G": 3, "T": 4}
    # s_num = [dict[S[i]] for i in range(len(S))]
    for pq in zip(P, Q):
        # answer.append(min(s_num[pq[0]:pq[1]+1]))
        if 'A' in S[pq[0]:pq[1]+1]:
            num = 1
        elif 'C' in S[pq[0]:pq[1]+1]:
            num = 2
        elif 'G' in S[pq[0]:pq[1]+1]:
            num = 3
        else:
            num = 4
        answer.append(num)

    return answer


print(solution(S="CAGCCTA", P=[2, 5, 0], Q=[4, 5, 6]))
