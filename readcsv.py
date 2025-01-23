import numpy as np
import matplotlib.pyplot as plt
import csv

distance = np.loadtxt('distances.csv', delimiter=',', dtype=float)
point = np.loadtxt('points.csv', delimiter=',', dtype=float)

plt.figure(figsize=(10,6))
plt.scatter(point[:, 0], point[:, 1], c=distance, cmap='viridis',s=20)
plt.colorbar()
plt.legend()
plt.show()
        


