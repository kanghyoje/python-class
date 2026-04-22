t = tuple(map(int, input().split()))

one = set()

for i in t:
  if t.count(i) == 1:
    one.add(i)

print(tuple(one))