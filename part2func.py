import numpy as np
import matplotlib.pyplot as plt

def f1(x,y):
    return x*y

def f2(x,y):
    return x**2 + y**2

def f3(x,y):
    return np.sin(3*x)*y

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z1 = f1(X,Y)
Z2 = f2(X,Y)
Z3 = f3(X,Y)

fig = plt.figure(figsize=(15, 5))

ax1 = fig.add_subplot(1,3,1, projection='3d')
surf1 = ax1.plot_surface(X, Y, Z1, cmap='viridis')
ax1.set_title('f1(x,y) = x*y')

ax2 = fig.add_subplot(1,3,2, projection='3d')
surf2 = ax2.plot_surface(X, Y, Z2, cmap='viridis')
ax2.set_title('f2(x,y) = x^2 + y^2')

ax3 = fig.add_subplot(1,3,3, projection='3d')
surf3 = ax3.plot_surface(X, Y, Z3, cmap='viridis')
ax3.set_title('f3(x,y) = sin(3x)*y')

plt.tight_layout()
plt.show()

