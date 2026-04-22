num = map(int, input().split())
짝수합 = 0
홀수합 = 0

for i in num:
  if i % 2 == 0:
    짝수합 += i
  else:
    홀수합 += i
print("짝수 합:" , 짝수합)
print("홀수 합:" , 홀수합)