"""
1. Stwórz listę 1000 losowych liczb z przedziału od 1 do 1000
2. Sprawdź ile jest liczb ciągu fibonacciego w powyższej liście
"""

import random
numbers = [random.randint(1, 1000) for _ in range(1000)]
print(numbers)

fib = [0, 1]
i = 1

while fib[i] <= 1000:
    fib.append((fib[i]) + fib[i - 1])
    i = i + 1
print(fib)

howManyInFibs = 0

for i in range(len(fib)):
    for j in range(len(numbers)):
        if fib[i] == numbers[j]:
            howManyInFibs += 1

print(howManyInFibs)