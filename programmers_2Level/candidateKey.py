# 후보키

# 학번, 이름, 전공, 학년
# 후보키 1)학번, 2)이름, 전공
from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    # 전체 조합
    candidates = []
    for i in range(1, col + 1):
        candidates.extend(combinations(range(col), i))
    print('전체조합', candidates)

    # 유일성 만족하는 조합
    # 유일성 판단은 열(학번, 이름..) 데이터가 중복 값 없이 테이블 '행' 만큼 동일하게 있다는 의미.
    # combi 사용하면 1개의 경우 ('데이터',) 형태로 콤마가 찍혀나온다. tuple 형태임 (type 함수로 확인)
    # 콤마를 제거하고 확인하려면 join 으로 합쳐주기
    unique = []
    for candi in candidates:
        tmp = [''.join([item[i] for i in candi]) for item in relation]
        # tmp2 = [[item[i] for i in candi] for item in relation]
        print(f'candi={candi}, tmp={tmp}')
        # print(f'test tmp2={tmp2}')

        if len(set(tmp)) == row:
            unique.append(candi)
    print('유일성 조합', unique, '길이=', len(unique))

    # 최소성 만족하는 조합
    # a.issubset(b) a는 b의 부분 집합인지 체크, True 인 경우 유일성이 깨지는 집합이다.
    # set 집합에서 discard는 전달받은 값을 삭제
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            print(unique[i], unique[j], '부분 집합=', set(unique[i]).issubset(set(unique[j])))
            if set(unique[i]).issubset(set(unique[j])):
                answer.discard(unique[j])

    return len(answer)


print(solution(relation=[["100", "ryan", "music", "2"],
              ["200", "apeach", "math", "2"],
              ["300", "tube", "computer", "3"],
              ["400", "con", "computer", "4"],
              ["500", "muzi", "music", "3"],
              ["600", "apeach", "music", "2"]]))
