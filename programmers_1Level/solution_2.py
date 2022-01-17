# 코딩테스트 고득점 Kit
# 정렬 
# Level 1) K번째수


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

answer = []
for i, j, k in commands:
    answer.append(sorted(array[i - 1:j])[k - 1])
    # print(f'현재 {i}, {j}, {k} :: {array[i-1:j]}')

print(answer)
print()

# 다른 사람의 풀이
# map(함수, 리스트) 사용법: 함수와 리스트를 인자로 받으며,
#                        리스트로부터 원소를 하나씩 꺼내서 함수를 적용시키고
#                        결과를 새로운 리스트에 담아주는 것

L = list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))
print(L)
