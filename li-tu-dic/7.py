N = int(input())

dic = {}
li_score = []

for i in range(N):
  name, score = input().split()
  score = int(score)
  dic[name] = score
  li_score.append(score)

  if i == 0:
    continue
  if li_score[i] >= li_score[i-1]:
    max_score = score
    max_name = name
  

  
print(max_name, max_score)