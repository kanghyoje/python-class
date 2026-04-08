hang = int(input("행 수: "))

star = 1
for i in range(hang, 0, -1):
  print(i * ' ' + star * "*" + i * ' ')
  star += 2