a = input().lower().split()
b = input().lower().split()

count_a = {}
for word in a:
  count_a[word] = count_a.get(word, 0) + 1

count_b = {}
for word in b:
  count_b[word] = count_b.get(word, 0) + 1

result = {}
for word in count_a:
  if word in count_b:
    result[word] = count_a[word] + count_b[word]

print(result)