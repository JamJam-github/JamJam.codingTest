# (04) 피보나치 순열


F0 = 0
F1 = 1


def fibo(n):
    if n < 2:
        return n

    answer = fibo(n - 1) + fibo(n - 2)
    return answer


def fibo_new(n):
    l, r, ans = 0, 1, 0
    for i in range(2, n + 1):
        ans = l + r
        print(f'f({i})은 = {ans}')
        l = r
        r = ans
    return ans

print(fibo_new(5))


def combi(n, m):
    return fibo(n) / (fibo(m) * fibo(n - m))

# print(combi(5, 2))
