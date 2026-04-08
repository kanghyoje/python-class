score = {'민수': 95, '지영': 82, '철수': 68}

for name in score:
  if score[name] >= 90:
    score[name] = 'A'
  elif score[name] >= 80:
    score[name] = 'B'
  else:
    score[name] = 'C'

print(score)