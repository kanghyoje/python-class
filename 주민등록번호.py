jumin = input()
front, back = jumin.split('-')

YY = front[0:2]
MM = front[2:4]
DD = front[4:6]

SE = int(back[0])

if SE not in [1,2,3,4,5,6,7,8]:
  print("잘못된 주민등록번호입니다.")
  exit()

if SE == 1 or SE == 3:
  print("대한민국 남성입니다.")
  if SE == 1:
    YE = 19
  else:
    YE = 20

elif SE == 2 or SE == 4:
  print("대한민국 여성입니다.")
  if SE == 2:
    YE = 19
  else:
    YE = 20

elif SE == 5 or SE == 7:
  print("외국인 남성입니다.")
  if SE == 5:
    YE = 19
  else:
    YE = 20

else:
  print("외국인 여성입니다.")
  if SE == 6:
    YE = 19
  else:
    YE = 20

year = int(str(YE) + YY)

if MM == "02":
  if DD == "29":
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
      print('윤년생일입니다.')
    else:
      print('잘못된 날짜입니다.')
  elif int(DD) > 28:
    print("잘못된 날짜입니다.")

print(f"생년월일은 {YE}{YY}년 {MM}월 {DD}일 입니다.")