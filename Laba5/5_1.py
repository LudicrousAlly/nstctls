import numpy as np

x = np.array([[3, 0, 1, 8], [2, -4, 2, 8], [3, 0, 0, 8], [0, 2, 3, 5]])

print(x)

p = 1

diag = x.diagonal()

for i in range(len(diag)):
    if int(diag[i]) != 0:
        p *= diag[i]

print("Произведение диагональных элементов равно: ", p)
