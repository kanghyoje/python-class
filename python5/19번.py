age = int(input('나이를 입력하세요:'))
cost = 14000
if age >= 60:
  print("30% 할인 대상입니다.")
  cost *= 0.7
elif age <= 10:
  print("20% 할인 대상입니다.")
  cost *= 0.8
else:
  print('할인 대상이 아닙니다.')
print('찜질방 이용 요금:', cost)