import numpy as np
import matplotlib.pyplot as plt
    
# Parametry hipocykloidy
R = 5  # Promień dużego okręgu
r = 2  # Promień małego okręgu
d = 3  # Odległość punktu od środka małego okręgu
    
# Kąty (pełny obrót dla hipocykloidy)
theta = np.linspace(0, 2 * np.pi * (R / np.gcd(R, r)), 1000)
    
# Obliczanie współrzędnych
x = (R - r) * np.cos(theta) + d * np.cos((R - r) / r * theta)
y = (R - r) * np.sin(theta) - d * np.sin((R - r) / r * theta)
    
    # Tworzenie wykresu
plt.figure(figsize=(8, 8))
    
# Kolorowanie linii – kolory zmieniają się wzdłuż wykresu
for i in range(len(theta) - 1):
    plt.plot(x[i:i+2], y[i:i+2], color=plt.cm.rainbow(i / len(theta)), linewidth=2)
    
plt.title('Kolorowa hipocykloida')
plt.axis('equal')
plt.grid(True)
plt.show()