num = int(input("자연수 입력: "))
count = 1

for i in range(1, num + 1):
  count *= i
print(f"{num}!은 120")