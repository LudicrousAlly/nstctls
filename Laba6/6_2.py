import numpy as np
import matplotlib.pyplot as plt
import glob
from itertools import chain

salt = []
temper = []

for file in glob.glob("C:\\Users\\ilyat\\Desktop\\University\\Python\\Laba6\\T[0-99].txt"):
    with open(file) as f:
        tmp = f.readlines()
        for i in range(len(tmp)):
            tmp[i] = int(tmp[i])
        temper.append(tmp)

for file in glob.glob("C:\\Users\\ilyat\\Desktop\\University\\Python\\Laba6\\S[0-99].txt"):
    with open(file) as f:
        tmp = f.readlines()
        for i in range(len(tmp)):
            tmp[i] = int(tmp[i])
        salt.append(tmp)

corr = []

for i in range(len(salt)):
    corr.append([0]*len(salt[i]))
    corr[i] = np.array(corr[i])

for i in range(len(salt)):
    corr[i] = np.corrcoef(temper[i], salt[i])

for i in range(len(salt)):
    print(corr[i])

temper = list(chain.from_iterable(temper))

salt = list(chain.from_iterable(salt))

plt.title("Поле значений")
plt.xlabel("Солёность")
plt.ylabel("Температура")
plt.grid(True, which='both')
plt.plot(salt, temper, "r.")
plt.xticks(range(22))
plt.yticks(range(22))
plt.ylim(0, 11)
plt.xlim(0, 10)
plt.show()