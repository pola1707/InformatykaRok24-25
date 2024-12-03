def fib(n):
    a = 1
    b = 1
    c = 0
    for i in range(n-2):
        c = a + b
        a = b
        b = c
    return c

def isPrime(n):
    result = True
    if n <= 0:
        result = False
        return result
    else:
        for i in range(2, n):
            if n % i == 0:
                result = False
                break
        return result

for i in range(40):
    liczbaZFib = fib(i)
    if isPrime(liczbaZFib) == True:
        print(liczbaZFib)