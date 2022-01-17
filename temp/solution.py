# 문제 (01) 리스트 원소 합
# 입력으로 주어지는 리스트 x의 첫 원소와 마지막 원소의 합을 리턴하는 함수
listN = int(input("리스트의 길이를 입력하세요:: "))
inputL = []
for n in range(listN):
    inputL.append(int(input("원소를 입력하세요:: ")))


def solution(x) -> object:
    print("첫 원소:: %d, 마지막 원소:: %d" % (x[0], x[len(x) - 1]))
    val = x[0] + x[len(x) - 1]
    print("최종 합:: " + str(val))


solution(inputL)
