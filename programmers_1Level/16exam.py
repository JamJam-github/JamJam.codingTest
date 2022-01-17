# 두 정수 사이의 합

answer = []

arr, divisor = [5, 9, 7, 10], 5
answer.sort()
print(sorted([k for k in arr if k % divisor == 0]) or [-1])


# 같은 숫자는 싫어
