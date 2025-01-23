import numpy as np
import matplotlib.pyplot as plt

hist = np.loadtxt('values_for_hist.csv', delimiter=',', dtype=float)
print(hist)
bins = 10
plt.figure(figsize=(10,6))
plt.hist(hist, bins, color='blue', edgecolor='black')
plt.show()