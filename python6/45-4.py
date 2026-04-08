hang = int(input("행 수: "))

space = 1
for i in range(hang, 0, -1):
  print(" " * space + "*" * i + " ")
  space += 1