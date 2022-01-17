# (05) 재귀적 이진탐색


L = [2, 3, 5, 6, 9, 11, 15]
x = 20
l = 0
u = 6


def binsearch(L, x, l, u):
    if u < l:
        return -1
    mid = (l + u) // 2

    print(f'Current l, u, mid: {l}, {u}, {mid}')

    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return binsearch(L, x, l, mid-1)
    else:
        return binsearch(L, x, mid+1, u)


print(binsearch(L, x, l, u))