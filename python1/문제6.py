s = 0
while True:
  num = input("숫자 입력 (종료는 n) : ")
  if num == 'n': # 입력 받는 문자가 n이면 / 종료
    break
  s += int(num) # s변수에 num을 정수로 받아서 계속 더해준다.
print("합계 : ", s)