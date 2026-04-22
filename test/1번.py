word = input()
count = 0
for ch in word.lower():
  if ch in ('a', 'e', 'i', 'o', 'u'):
    count += 1
print("모음 개수:", count)