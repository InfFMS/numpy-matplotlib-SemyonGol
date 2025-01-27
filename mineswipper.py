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

from matplotlib.pyplot import legend

#Создадим поле и введём необходимые переменные
mine = np.zeros((11, 11))
m, c = 2, 0
dicC, dicX, dicY = {}, {}, {}

#Разместим 15 мин в рандомные координаты поля
while m < 17:
    dicX[m-2] = randint(0, 10)
    dicY[m-2] = randint(0, 10)
    if c > 0:       #Необходимо для создания второй пары координат(см. ниже)
        for i in range(0, m-2):
            for o in range(i+1, m-1):
                if dicX[i] == dicX[o] and dicY[i] == dicY[o]:   #Если пары координат мин совпадают, то они "сольются"
                    dicX[o] = randint(0, 10)              #в одну мину. Для этого проверим на наличие таких пар
                    dicY[o] = randint(0, 10)              #и изменим их на другие
    dicC[m-2] = plt.Circle((dicX[m-2], dicY[m-2]), 0.45, color='r', fill=True)
    ax = plt.gca()
    ax.add_patch(dicC[m-2])
    m += 1
    c += 1

#Создадим функции, которые будут увеличивать значение клетки
#при различных положениях мины: по центру, слева, сверху, справа,
#снизу, нижний левый угол, левый верхний, правый верхний, правый нижний
def centre(M, Y, X):
    M[Y-1, X-1] += 1
    M[Y, X-1] += 1
    M[Y+1, X-1] += 1
    M[Y+1, X] += 1
    M[Y+1, X+1] += 1
    M[Y, X+1] += 1
    M[Y-1, X+1] += 1
    M[Y-1, X] += 1
    return M
def left(M, Y, X):
    M[Y-1, X] += 1
    M[Y-1, X+1] += 1
    M[Y, X+1] += 1
    M[Y+1, X+1] += 1
    M[Y+1, X] += 1
    return M
def top(M, Y, X):
    M[Y, X-1] += 1
    M[Y+1, X-1] += 1
    M[Y+1, X] += 1
    M[Y+1, X+1] += 1
    M[Y, X+1] += 1
    return M
def right(M, Y, X):
    M[Y-1, X] += 1
    M[Y-1, X-1] += 1
    M[Y, X-1] += 1
    M[Y+1, X-1] += 1
    M[Y+1, X] += 1
    return M
def bottom(M, Y, X):
    M[Y, X-1] += 1
    M[Y-1, X-1] += 1
    M[Y-1, X] += 1
    M[Y-1, X+1] += 1
    M[Y, X+1] += 1
    return M
def bottomleft(M):
    M[9, 0] += 1
    M[9, 1] += 1
    M[10, 1] += 1
    return M
def topleft(M):
    M[1, 0] += 1
    M[1, 1] += 1
    M[0, 1] += 1
    return M
def topright(M):
    M[0, 9] += 1
    M[1, 9] += 1
    M[1, 10] += 1
    return M
def bottomright(M):
    M[10, 9] += 1
    M[9, 9] += 1
    M[9, 10] += 1
    return M

#Условия для активации верхних функций
for i in range(0, 15):
    if dicX[i] == 0:
        if dicY[i] == 0:
            topleft(mine)
        if dicY[i] == 10:
            bottomleft(mine)
        else:
            left(mine, dicY[i], dicX[i])
    elif dicY[i] == 0:
        if dicX[i] == 10:
            topright(mine)
        elif dicX[i] == 0:
            topleft(mine)
        else:
            top(mine, dicY[i], dicX[i])
    elif dicX[i] == 10:
        if dicY[i] == 10:
            bottomright(mine)
        elif dicY[i] == 0:
            topright(mine)
        else:
            right(mine, dicY[i], dicX[i])
    elif dicY[i] == 10:
        if dicX[i] == 0:
            bottomleft(mine)
        if dicX[i] == 10:
            bottomright(mine)
        else:
            bottom(mine, dicY[i], dicX[i])
    else:
        centre(mine, dicY[i], dicX[i])

#Заменим значения клеток под минами на 0, так как
#под ними клетка не может иметь числовое значение
for i in range(0, 15):
    mine[dicY[i], dicX[i]] = 0

#Визуализируем всё поле
plt.imshow(mine, cmap='Blues')
plt.title('Сапёр')
plt.xlabel('Чем холоднее синий цвет, тем больше мин около клетки')
plt.ylabel('Красным отмечены мины')
plt.show()
