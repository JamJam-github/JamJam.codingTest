# 퀵 정렬
# 시간복잡도 O(NlogN)를 보장한다.
# 분할하는 방식
# 리스트의 첫 번째를 pivot 으로 선정하고
# pivot보다 작은 숫자를 왼쪽으로, 큰 숫자를 오른쪽으로 교환한다.

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [i for i in tail if i <= pivot]
    right = [i for i in tail if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(array))
