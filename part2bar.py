import numpy as np
import matplotlib.pyplot as plt

values = np.loadtxt('values_for_bars.csv', delimiter=',', dtype=float)
unique_values, counts = np.unique(values, return_counts=True)

plt.figure(figsize=(10,6))
plt.bar(unique_values, counts, color='blue', label='Frequency')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()