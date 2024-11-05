a, b = map(int, input().split())
if a == 0:
    if b == 0:
        print("NWR")
    else:
        print("BR")
else:
    x = b / a * -1
    print(f"{x:0.2f}")
