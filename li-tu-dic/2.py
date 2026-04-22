짝수 = []
홀수 = []


while True:
  li = list(map(int,input().split()))

  for i in range(len(li)):
    if li[i] % 2 == 0:
      짝수.append(li[i])
    else:
      홀수.append(li[i])
  break
print(짝수)
print(홀수)