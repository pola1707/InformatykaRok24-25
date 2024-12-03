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

print(series)

lenght = len(f'{series[-1]}')
for i in range(0, len(series)):
    inlenght = len(series[i])
    for k in range(inlenght, lenght):
        series[i] = '0' + f'{series[i]}'
    print(series[i])

print(*series, sep='\n')