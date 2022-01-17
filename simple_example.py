import numpy as np
import matplotlib.pyplot as plt
import pyro

x1 = np.random.normal(2, 0.3, 70)
x2 = np.random.normal(6, 1, 150)
x = np.hstack((x1, x2))

plt.hist(x, bins=40)
plt.grid()
plt.show()
print('Change from work.')