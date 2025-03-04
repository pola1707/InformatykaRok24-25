import numpy as np
import matplotlib.pyplot as plt

# Parametry
R = 5  # Promień większego okręgu
r = 3  # Promień mniejszego okręgu

# Zakres kąta
theta = np.linspace(0, 2 * np.pi, 1000)

# Równania hipocykloidy
x = (R - r) * np.cos(theta) + r * np.cos((R - r) / r * theta)
y = (R - r) * np.sin(theta) - r * np.sin((R - r) / r * theta)

# Rysowanie
plt.figure(figsize=(6, 6))
plt.plot(x, y)
plt.title("Hipocykloida")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')
plt.grid(True)
plt.show()
