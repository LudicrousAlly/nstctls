import numpy as np

x = np.array([5, 1, 0, 3, 0, 0, 5, 0, 12, 11])

nzz = np.nonzero(x)
em = []
max = 0

print("Индексы ненулевых элемов: ", nzz[0])

for i in range(1, len(x)):
    if i in nzz[0] and (i - 1) not in nzz[0]:
        em.append(x[i])

em = np.array(em)

print("Максимальный элемент, перед которым стоит нулевой: ", em.max())