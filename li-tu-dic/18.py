N = int(input())
score_dict = {'A':0, 'B':0, 'C':0, 'D':0}
for i in range(N):
  name, score = input().split()
  score = int(score)
  if score >= 90:
    score_dict['A'] += 1
  elif score >= 80:
    score_dict['B'] += 1
  elif score >= 70:
    score_dict['C'] += 1
  else:
    score_dict['D'] += 1
print(score_dict)