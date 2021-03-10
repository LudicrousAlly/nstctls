import numpy as np
import scipy.spatial

x = np.array([[1, 3, 2], [2, 4, 3], [5, 4, 2], [5, 4, 6], [5, 6, 7]])
y = np.array([[6, 8, 7], [7, 9, 9], [10, 9, 8]])

print(scipy.spatial.distance.cdist(x,y, metric='euclidean'))

rast = []
for i in range(len(x)):
    rast.append([0]*len(y))

for i in range(len(rast)):
    for j in range(len(rast[i])):
        rast[i][j] = scipy.spatial.distance.euclidean(x[i], y[j])

print("\n--------------------------------\n\nRast:")
for i in range(len(rast)):
    print(rast[i])
