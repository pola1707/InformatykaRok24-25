import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y = 2*x**2 - 3
plt.plot(x,y)
plt.show()