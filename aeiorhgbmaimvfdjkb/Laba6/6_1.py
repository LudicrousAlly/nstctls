import numpy as np
import matplotlib.pyplot as plt

temper = []

with open("t.txt") as f:
    temper = f.readlines()

for i in range(len(temper)):
    temper[i] = int(temper[i].split()[0])

salt = []

with open("s.txt") as f:
    salt = f.readlines()

for i in range(len(salt)):
    salt[i] = int(salt[i].split()[0])

corr = [0]*len(salt)

corr = np.array(corr)

corr = np.corrcoef(temper, salt)

print(corr)

plt.title("Поле значений")
plt.xlabel("Солёность")
plt.ylabel("Температура")
plt.grid(True, which='both')
plt.plot(salt, temper, "r.")
plt.xticks(range(22))
plt.yticks(range(22))
plt.show()