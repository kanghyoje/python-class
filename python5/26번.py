point = 0
sum = 0
while sum < 20:
  point = int(input('다크 점수를 입력하세요:'))
  print('이번 점수는', point)
  sum += point
print('합계 점수는', sum)