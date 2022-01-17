# 기존
t = list(range(10))
print(t)

import numpy as np

n1 = np.array([1, 2, 3, 4, 5])
print(n1)
n2 = np.array([3, 1.4, 2, 3, 4])
print(n2)
n3 = np.array([1, 2, 3, 4], dtype='float')
print(n3)
n3.astype(int)
print(n3)