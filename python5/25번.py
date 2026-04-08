hap = 0
while True:
  num = int(input('숫자입력:'))
  hap += num
  if hap >= 20:
    break
print('입력한 수의 합은:', hap)