import matplotlib.pyplot as plt
from random import randint
import numpy as np
T, days = [], []
cold = np.array([])
hot = np.array([])
daysC, daysH = [], []
T += [randint(-25, 30)
      for x in range(0, 365)]

for i in range(0, 363):
    days += [i+1]
days += [364] + [365]

for i in range(1, 365):
    if T[i] <= 0:
        cold = np.append(cold, T[i])
        daysC += [days[i]]
    else:
        hot = np.append(hot, T[i])
        daysH += [days[i]]
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_axes([0.1, 0.3, 0.8, 0.6])
ax1.plot(days, T)
plt.scatter(daysC, cold, color='Blue')
plt.scatter(daysH, hot, color='Red')
plt.show()