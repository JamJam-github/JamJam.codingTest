# (02) 정렬된 리스트에 원소 삽입
# 리스트 L 과 정수 x 가 인자로 주어질 때,
# 리스트 내의 올바른 위치에 x 를 삽입하여 그 결과 리스트를 반환하는 함수 solution 을 완성하세요.

L = [20, 37, 58, 72, 91]
x = 65


def solution(L, x):
    for idx, num in enumerate(L):
        if L[-1] < x:
            L.append(x)
            break

        if x < num:
            print("해당 인덱스에 삽입합니다.")
            L.insert(idx, x)
            break
        else:
            print(num, "<", x, "pass")
            pass

    return L


print(solution(L, x))
