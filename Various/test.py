import numpy as np


N = 5
a = np.array([1, 2, 3, 4, 5, 6])
b = np.empty(N+1)

# Typowy sposob na taka sume
# for i in range(1, N):
#     b[i] = a[i+1] + a[i-1] - a[i]

# Sposob z indeksowaniem
b = np.array(a[:-2] + a[2:] - a[1:-1])

print(b)
