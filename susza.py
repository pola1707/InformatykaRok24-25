precipitation = [12, 0, 0, 23, 45, 2, 3, 0, 0, 0, 0, 3, 4, 0, 0, 0, 2, 1, 0, 2]
temporary = [0] * len(precipitation)

for i in range(1, len(precipitation)):
    if precipitation[i] == 0:
        temporary[i] = temporary[i-1] + 1
print(max(temporary))
