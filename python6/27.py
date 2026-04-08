import random

com1 = random.randint(1, 6)
com2 = random.randint(1, 6)

com_list = [com1, com2]
user = input('숫자 2개입력:')
user = list(map(int, user.split(' ')))

if com1 in user and com2 in user:
  print("1등!")
elif com1 in user or com2 in user:
  print("2등")
else:
  print("3등")