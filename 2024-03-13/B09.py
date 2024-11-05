n = int(input())
x = []

for _ in range(n):
  i = int(input())
  x.append(i)
x = sorted(x)
x[:n]

l = int(len(x))

if l%2 == 0:
  a = x[l//2-1:l//2+1]
  r = sum(a)/2
  print(f"{r:.1f}")
else:
  print(x[int(l//2)])