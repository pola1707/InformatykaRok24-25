import random as rnd

numbers = []
for i in range(10):
    n = rnd.randint(1, 100)
    numbers.append(n)

print(numbers)
print(*numbers)

print(sorted(numbers))
print(numbers)

numbers.sort()
print(numbers)

numbers = numbers[::-1]
print(numbers)

print(numbers[2:5])
print(numbers[1:6:2])
print(numbers[6:1:-1])

