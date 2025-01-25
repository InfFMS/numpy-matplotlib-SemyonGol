# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.

import matplotlib.pylab as plt
import numpy as np

chess = np.zeros((8, 8))
c = 0
Mx, My = [], []

while c <= 7:
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

for i in range(0, 8):
    Mx += [i]
    My += [i]

plt.plot(X, Mx, c='r')
plt.plot(My, Y, c='r')
plt.imshow(chess, cmap='Blues')
plt.show()