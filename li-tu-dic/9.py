a = input().split()
vowels = 'aeiou'

for word in a:
  count = 0
  for char in word.lower():
    if char in vowels:
      count += 1
  print(word, count)