num = int(input("숫자를 입력하세요:"))
sum = 1
for i in range(1, num+1): # 1부터 num까지의 수를 i에 넣는다. 1 2 3 4 5
  sum = sum * i # sum에 1부터 num까지의 수를 계속 곱하여 대입한다(팩토리얼). 
print(num, "!=", sum) # 팩토리얼 값을 출력한다.