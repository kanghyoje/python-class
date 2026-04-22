N = int(input())
sum = 0
li = []
for i in range(N):
  score = int(input())
  sum += score
  li.append(score)
  if i == 0:
    continue
  
  
  if li[i] > li[i-1]:
    max_score = li[i]
  if li[i] < li[i-1]:
    min_score = li[i]

average = int(sum / N)
print(f"총점: {sum}")
print(f"평균: {average}")
print(f"최고: {max_score}")
print(f"최저: {min_score}")