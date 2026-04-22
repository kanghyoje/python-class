N = int(input())

for i in range(N):
  a, b = input().split()
  b = int(b)

  if b >= 80:
    print(a, "합격")
  else:
    print(a, "불합격")