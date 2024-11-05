n = int(input())

sum = 0
numerator = -1
for i in range(n):
    numerator *= -1    # numerator = numerator * (-1)
    denominator = 2 * i + 1
    sum += numerator/denominator
print(f"PI wynosi {sum*4}")