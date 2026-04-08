words = ['a', 'b', 'a']

result = {}

for w in words:
  if w in result:
    result[w] += 1
  else:
    result[w] = 1

print(result)