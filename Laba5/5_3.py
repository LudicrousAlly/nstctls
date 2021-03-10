import numpy as np

a = np.loadtxt("A.txt", dtype=float)
b = np.loadtxt("B.txt", dtype=float)

a_ = np.linalg.inv(a)
x = np.dot(a_, b)

np.set_printoptions(suppress=True, precision=3)

np.savetxt("X.txt", x, fmt='%1.2f')