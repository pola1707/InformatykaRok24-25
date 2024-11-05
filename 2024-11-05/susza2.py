with open("dane.csv", "r") as file:
    data = file.readlines()

dataProcessed = []
for d in data:
    d = d.strip()
    d = d.split(";")
    record = []
    record.append(d[0])
    record.append(int(d[1]))
    dataProcessed.append(record)

drought = [0] * len(dataProcessed)
if dataProcessed[0][1] == 0:
    drought[0] = 1
for i in range(1, len(dataProcessed)):
    if dataProcessed[i][1] == 0:
        drought[i] = drought[i-1] + 1

max = drought[0]
for i in range(1, len(drought)):
    if max < drought[i]:
        max = drought[i]
        maxPosition = i

dateStart = dataProcessed[maxPosition - max + 1][0]
dateEnd = dataProcessed[maxPosition][0]

print(f'{dateStart}')
print(f'{dateEnd}')