# 큰 수 만들기
# 문자열 순서를 그대로 가져가야함.
# if stack[-1] < value then pop & count++
# if stack[-1] >= value then push


def solution(number, k):
    answer = []
    count = 0

    for index, value in enumerate(number):
        if not answer:
            answer.append(value)
        else:
            if count != k:
                while answer[-1] < value:
                    answer.pop()
                    count += 1
                    if not answer or count == k:
                        break

            answer.append(value)
    if count != k:
        answer = answer[:-k]
    return ''.join(answer)


print(solution(number="1924", k=2))
print(solution(number="1231234", k=3))
print(solution(number="4177252841", k=4))
print(solution(number="4", k=1))
print(solution(number="999", k=2))
