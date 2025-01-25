from random import randint
import numpy as np

M = np.zeros((11, 11))

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

y = 5
x = 0
M[y, x] += 2
if x == 0:
    if y == 0:
        print(topleft(M))
    if y == 10:
        print(bottomleft(M))
    else:
        print(left(M, y, x))
elif y == 0:
    if x == 10:
        print(topright(M))
    if x == 0:
        print(topleft(M))
    else:
        print(top(M, y, x))
elif x == 10:
    if y == 10:
        print(bottomright(M))
    if y == 0:
        print(topright(M))
    else:
        print(right(M, y, x))
elif y == 10:
    if x == 0:
        print(bottomleft(M))
    if x == 10:
        print(bottomright(M))
    else:
        print(bottom(M, y, x))
else:
    print(centre(M, y, x))