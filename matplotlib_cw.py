import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return x ** 2

def f2(x):
    return np.sin(x)

def f3(x):
    return np.arctan(x)

x = np.linspace(-2, 2, 100)
y1 = f1(x)
y2 = f2(x)
y3 = f3(x)

plt.plot(x, y1, label='x^2')
plt.plot(x, y2, label='sin(x)')
plt.plot(x, y3, label='arctan(x)')
plt.legend()
plt.show()
