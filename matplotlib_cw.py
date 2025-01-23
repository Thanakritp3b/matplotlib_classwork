import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return x ** 2

def f2(x):
    return x * np.sin(2 * x)

def f3(x):
    return np.arctan(x)

x = np.linspace(-2, 2, 100)
y1 = f1(x)
y2 = f2(x)
y3 = f3(x)

plt.plot(x, y1, label='x^2', color='red', marker='*', markersize=2)
plt.plot(x, y2, label='sin(x)', color='green', linestyle='dashed', marker='o', markersize=2)
plt.plot(x, y3, label='arctan(x)', color='blue', linestyle='dotted', marker='x', markersize=2)
plt.legend()
plt.show()
