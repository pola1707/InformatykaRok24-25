def fib(n):
    a = 1
    b = 1
    c = 1
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return c

series = []
binary = 0
for i in range(1, 40):
    series.append(bin(fib(i))[2:])

for j in range(0, len(series)):
    count = series[j].count('1')
    if count == 6:
        print(series[j])