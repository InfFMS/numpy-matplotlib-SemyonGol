# Задача:
# Создайте игровое поле для "Сапёра" размером 10×10.
# Поле должно быть представлено в виде двумерного массива.
# Разместите 15 мин случайным образом (обозначьте их числом −1).
# Для каждой клетки без мины подсчитайте количество мин в соседних клетках.
# Визуализируйте:
# Само поле (где мины выделены красным).
# Поле с числами, где указано количество мин вокруг каждой клетки (для наглядности).
#

import numpy as np
import matplotlib.pyplot as plt
from random import randint

mine  = np.zeros((11, 11))
m = 2
c = 0
dicC = {}
dicA = {}
dicB = {}

while m < 17:
    dicA[m-2] = randint(0, 10)
    dicB[m-2] = randint(0, 10)
    if c > 0:
        for i in range(0, m-2):
            for x in range(i+1, m-1):
                if dicA[i] == dicA[x] and dicB[i] == dicB[x]:
                    dicA[x] = randint(0, 10)
                    dicB[x] = randint(0, 10)
    dicC[m-2] = plt.Circle((dicA[m-2], dicB[m-2]), 0.45, color='r', fill=True)
    ax = plt.gca()
    ax.add_patch(dicC[m-2])
    m += 1
    c += 1

plt.imshow(mine, cmap='Blues')
plt.show()