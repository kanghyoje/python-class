a = set()

for i in range(10):
  num = int(input())

  a.add(num % 42)
print(len(a))