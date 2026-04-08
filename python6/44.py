행 = int(input("행 수: "))
열 = int(input("열 수: "))

for i in range(1, 행 + 1):
  for j in range(1, 열 + 1):
    print(i * j, end=' ')
  print()