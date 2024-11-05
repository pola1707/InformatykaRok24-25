a, b, c = map(float, input().split())
if a+b>c:
  if b+c>a:
    if a+c>b:
      print("Tak")
    else:
      print("Nie")
  else:
    print("Nie")
else:
  print("Nie")