import matplotlib.pylab as plt
import numpy as np
x = np.arange(10)
y1 = np.random.randint(3, 20, len(x))
y2 = np.random.randint(3, 20, len(x))
w = 0.3
x.bar(x - w/2, y1, width=w)
x.bar(x + w/2, y2, width=w)