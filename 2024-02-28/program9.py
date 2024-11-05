i = 1
potega = 1
n, k = map(float, input().split())
while i <= k:
  potega = potega * n
  i = i+1

print(f"{potega:0.0f}")
