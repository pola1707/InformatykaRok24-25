
def fib(n):
    a = 1
    b = 1
    c = 0
    for i in range(n-2):
        c = a + b
        a = b
        b = c
    return c

print(fib(10))
print(fib(20))
print(fib(30))
print(fib(40))
