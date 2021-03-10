import numpy as np
import scipy.stats
import math

x = np.array([[1, 3, 4],
              [4, 3, 5],
              [6, 4, 5],
              [4, 7, 6],
              [5, 8, 7]])

m = [2.4, 5.6, 3.9]

c = [[10, 4, 5],
     [4, 10, 6],
     [4, 7, 6]]

print("scipy.stats.multivariate_normal(m, c).logpdf(x) = ", scipy.stats.multivariate_normal(m, c).logpdf(x))

array = [0]*len(x)


det = np.linalg.det(c)
c_1 = np.linalg.inv(c)


for i in range(len(x)):

    sum = 0

    for j in range(len(m)):
        for k in range(len(m)):
            sum += (x[i][j] - m[j]) * c_1[j][k] * (x[i][k] - m[k])


    array[i] = np.e**( (-1/2) * sum ) / ( (math.sqrt(2 * np.pi))**len(m) * math.sqrt(det) )


for i in range(len(array)):
    array[i] = np.log(array[i])

print("\t\t\t\t\t\t\t\t\t\tln(arr) = ", array)
