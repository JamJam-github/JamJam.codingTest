# [3차] 압축

# 인덱스부터 1씩 증가해서 사전에 이미 존재하는 경우
# w에 문자열을 추가, 없으면 사전에 새로 등록

def solution(msg):
    answer = []
    # A ~ Z까지 사전만들기
    dic = {chr(64 + i): i for i in range(1, 27)}
    count = 27

    idx_f, idx_e = 0, 0
    while True:
        idx_e += 1

        # 처리되지 않은 글자 O에 해당하는 색인 번호를 출력한다.
        if idx_e == len(msg):
            answer.append(dic[msg[idx_f:idx_e]])
            break

        # 가장 긴 문자열을 가지고 사전에 없는 단어를 찾은 경우
        # 사전에 추가하고, 이전 문자열은 사전에 있으니 색인 번호를 출력해준다.
        if msg[idx_f:idx_e + 1] not in dic.keys():
            dic[msg[idx_f:idx_e + 1]] = count
            count += 1
            answer.append(dic[msg[idx_f:idx_e]])
            idx_f = idx_e

    return answer


print(solution(msg="TOBEORNOTTOBEORTOBEORNOT"))
