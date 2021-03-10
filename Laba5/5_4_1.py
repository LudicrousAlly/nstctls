import numpy as np
import matplotlib.pyplot as plt

array = np.random.randint(0, 255, (4, 4, 3))

print("array = ", array, "\n\n\n")

vector = np.random.randint(0, 255, 3)

print("vector = ", vector, "\n\n\n")

fig, ax = plt.subplots()

fig1, ax1 = plt.subplots()

ax.imshow(array)

for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j] += vector

        for k in range(len(array[i][j])):
            if array[i][j][k] > 255:
                array[i][j][k] -= 255


print("array + vector = ", array, "\n\n\n")

plt.figure(2)

ax1.imshow(array)

plt.show()