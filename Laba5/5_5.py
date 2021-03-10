import numpy as np

x = np.array([1, 2, 2, 3, 5, 3, 5, 3, 4, 1])

_x_, counts = np.unique(x, return_counts=True)

print(_x_)
print(counts)
