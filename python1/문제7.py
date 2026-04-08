num = int(input('숫자를 입력하세요:'))
for i in range(0, 101, 10): # i변수에 10의 배수를 대입한다.
  if num == i and num % 3 != 0: # 만약 num이 10의 배수이고 3의 배수가 아니라면 / 출력하시오.
    print(num)  

print('종료합니다.')