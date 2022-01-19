# 0과 1로만 이루어진 문자열 S를 가지고
# 모두 0, 혹은 모두 1로 만드는 최소한의 횟수

def solution(S):
    # min(0을 1로 바꾸는 횟수, 1을 0으로 바꾸는 횟수)
    count0 = 0
    count1 = 0
    if S[0] == '0':
        count0 += 1
    else:
        count1 += 1

    for i in range(1, len(S) - 1):
        # 다음 숫자가 달라지는 경우
        # 1로 달라진 경우 0으로 바꾸는 횟수를 늘려야 하고
        # 0으로 달라진 경우 1로 바꾸는 횟수를 늘려야 한다.
        if S[i] != S[i + 1]:
            if S[i + 1] == '1':
                count0 += 1
            else:
                count1 += 1

    return min(count0, count1)


print(solution(S='0001100'))
