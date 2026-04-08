num = int(input('수를 입력하세요:'))
odd = 0
even = 0

for i in range(1, num+1):
  if i % 2 == 1:
    odd += i
  else:
    even += i
print('1부터', num, '까지 홀수의 합은', odd)
print('1부터', num, '까지 짝수의 합은', even)