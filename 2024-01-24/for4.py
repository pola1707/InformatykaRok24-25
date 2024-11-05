for a in range(1,1000):
    for b in range(a, 1000):
        for c in range(b,1000):
            if a*a + b*b == c*c  or a*a + c*c == b*b or  b*b + c*c == a*a:
                print(a,b,c)