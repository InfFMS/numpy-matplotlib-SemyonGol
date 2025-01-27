# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.

from random import randint
import matplotlib.pyplot as plt
import numpy as np

C25 = 0
T, eq, days, daysC, daysH = [], [], [], [], []
cold = np.array([])
hot = np.array([])
dicEQ = {}
u = 0

T += [randint(-25, 30)
      for x in range(0, 365)]

print('Average:', sum(T)/len(T))

for i in range(0, 363):
    if T[i] > 25:
        C25 += 1
    days += [i+1]
print('T>25:', C25)
days += [364] + [365]

for o in range(1, 364):
    if T[o-1] < 0 and T[o] < 0:
        eq += [T[o-1], T[o]]
        u += 1
        dicEQ[u] = eq
    if T[o+1] >= 0:
        eq = []
EQ = dicEQ[1]
for i in range(1, len(dicEQ)):
    if len(dicEQ[i]) > len(EQ):
        EQ = dicEQ[i+1]
print('Longest sequence of T<0: ', EQ, ': ', len(EQ), sep='')

T = np.array(T)
unic = np.unique(T)
daysT = np.zeros(len(unic))
for u in range(0, len(unic)):
    for t in range(0, 365):
        if T[t] == unic[u]:
            daysT[u] += 1

for i in range(1, 365):
    if T[i] <= 0:
        cold = np.append(cold, T[i])
        daysC += [days[i]]
    else:
        hot = np.append(hot, T[i])
        daysH += [days[i]]

fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4])
ax1.bar(unic, daysT)
ax2 = fig.add_axes([0.1, 0.05, 0.8, 0.4])
ax2.plot(days, T)
plt.scatter(daysC, cold, color='Blue')
plt.scatter(daysH, hot, color='Red')
plt.show()

