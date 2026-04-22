a = input().lower().split()
count = {}

for word in a:
  count[word] = count.get(word, 0) + 1

for word, cnt in count.items():
  print(word, cnt)