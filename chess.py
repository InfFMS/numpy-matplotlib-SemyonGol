# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.

import matplotlib.pylab as plt
import numpy as np

chess = np.zeros((8, 8))
c = 0
dicX, dicY, dicC1, dicC2 = {}, {}, {}, {}

while c <= 7:       #Зададим массив из 0 и 1 в шахматном порядке
    for i in range(8):
        if c%2 == 0 and i%2 == 1:
            chess[c, i] += 1
        if c%2 == 1 and i%2 == 0:
            chess[c, i] += 1
    c += 1
print('Please, enter x coordinate of queen:', end= ' ')
x = int(input())
X = np.full(8, x)
print('Please, enter y coordinate of queen:', end= ' ')
y = int(input())
Y = np.full(8, y)


for i in range(0, 8):       #Нарисуем кружки по oX и oY, на которые может ходить наш ферзь
    dicX[i] = plt.Circle((i, y), 0.3, color='Yellow')
    dicY[i] = plt.Circle((x, i), 0.3, color='Yellow')
    ax = plt.gca()
    ax.add_patch(dicX[i])
    ax.add_patch(dicY[i])

c = y-1
b = y+1
for a in range(x+1, 8):     #Нарисуем кружки по диагональным осям справа от точки (x,y)
    dicC1[a] = plt.Circle((a, b), 0.3, color='Yellow')
    dicC1[a+7] = plt.Circle((a, c), 0.3, color='Yellow')
    ax = plt.gca()
    ax.add_patch(dicC1[a])
    ax.add_patch(dicC1[a+7])
    b += 1
    c -= 1
a = x-1
b = y+1
c = y-1
while a >= 0:       #Нарисуем кружки по диагональным осям слева от точки (x,y)
    dicC2[a] = plt.Circle((a, b), 0.3, color='Yellow')
    dicC2[a+7] = plt.Circle((a, c), 0.3, color='Yellow')
    ax = plt.gca()
    ax.add_patch(dicC2[a])
    ax.add_patch(dicC2[a + 7])
    b += 1
    c -= 1
    a -= 1

plt.imshow(chess, cmap='Blues')     #Визуализируем карту
plt.show()