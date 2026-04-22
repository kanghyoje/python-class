N = int(input())
total = 0
dic = {}
for i in range(N):
  name, score = input().split()
  score = int(score)
  total += score
  dic[name] = score

average = total / N

for j in dic:
  if dic[j] >= average:
    print(j, dic[j])