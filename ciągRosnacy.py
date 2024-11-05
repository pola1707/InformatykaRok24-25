"""
Znajdź najdłuższy spójny ciąg liczb rosnących
"""

data = [1, -3, 0, 2, 3, 5, 4, 1, 2, 1, 2, 3, 4, 5, 6, 7, 9, 9, 1, 0, 2]
temp = [1] * len(data)
max = temp[0]

for i in range(1, len(data)):
    if data[i] > data [i-1]:
        temp[i] = temp[i -1] + 1
print(temp)

for i in range(1, len(temp)):
    if temp[i] > max:
        max = temp[i]
        positionMax = i
print(max)

for i in range(positionMax - max + 1, positionMax + 1):
    print(data[i], end='')
