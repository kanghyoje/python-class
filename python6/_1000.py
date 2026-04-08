juice = 5

while True:
  print("====================")
  money = int(input("돈을 넣어주세요: "))
  if money >= 800:
    change = money - 800

    if change == 0:
      print("맛있는 주스 드세요.")
      juice -= 1

    else:
      print(f"맛있는 주스 드시고 잔돈 {change}원 받아 가세요.")
      juice -= 1

    if juice == 0:
      print("주스가 매진되었습니다.")
      break

  else:
    print("가격을 확인하세요.")
    print(money)

    if juice == 0:
      print("주스가 매진되었습니다.")
      break