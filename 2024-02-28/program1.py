import math

a, d = map(float, input().split())
b = math.sqrt(d**2 - a**2)
P = a * b
Ob = 2 * (a+b)
print(f"{P:0.2f}")
print(f"{Ob:0.2f}")
