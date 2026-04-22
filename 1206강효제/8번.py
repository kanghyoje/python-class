N = int(input())
sum = 0
pas = 0
for i in range(N):
  score = int(input())
  sum += score

  if score >= 80:
    pas += 1

print("평균:", sum / N)
print("합격자 수:", pas)