word1 = input()
word2 = input()

중복1 = set()
중복2 = set()

for c in word1:
  if word1.count(c) > 1:
    중복1.add(c)

for c in word2:
  if word2.count(c) > 1:
    중복2.add(c)

print(중복1)
print(중복2)