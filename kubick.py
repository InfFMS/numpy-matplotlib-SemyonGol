# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.

from random import randint
import numpy as np
import matplotlib.pyplot as plt

P1 = np.array([])
P2 = np.array([])
P3 = np.array([])
P4 = np.array([])
P5 = np.array([])
P6 = np.array([])
P = np.array([])
c = 0
eq = 0
maxx = 0
dic = {}
dic2 = {}
N = []
U = []

while c < 1000:
    a = randint(1, 6)
    if a == 1:
        P1 = np.append(P1, a)
    elif a == 2:
        P2 = np.append(P2, a)
    elif a == 3:
        P3 = np.append(P3, a)
    elif a == 4:
        P4 = np.append(P4, a)
    elif a == 5:
        P5 = np.append(P5, a)
    elif a == 6:
        P6 = np.append(P6, a)
    P = np.append(P, a)
    c += 1
M = [P1, P2, P3, P4, P5, P6]

for x in range(1, 7):
    for o in range(1, 999):
        if P[o-1] == P[o] == x:
            eq += 1
            maxx = eq + 1
        if P[o] != P[o+1]:
            eq = 0
    dic2[str(x-1)] = maxx
    eq = 0

for i in range(0, 6):
    dic[str(i)] = len(M[i])/1000
    print(i+1, ': ', len(M[i]), ', Probability:', end=' ', sep= '')
    i = str(i)
    print(dic[i], ', Amount of equal numbers in a row: ', dic2[i], sep='')
    N = N + [dic[i]]
    U = U + [dic2[i]]

cat = ['1','2', '3', '4', '5', '6']
val1 = ([len(P1), len(P2), len(P3), len(P4), len(P5), len(P6)])

fig, ax = plt.subplots(1, 5)
ax[0].bar(cat, val1, color='purple')
ax[0].set_xlabel('Значения')
ax[0].set_ylabel('Кол-во выпадений')
ax[2].bar(cat, N)
ax[2].set_xlabel('Значения')
ax[2].set_ylabel('Вероятность выпадений')
ax[4].bar(cat, U)
ax[4].set_xlabel('Значения')
ax[4].set_ylabel('Макс. кол-во одинак. подряд идущ. эл.')
plt.show()