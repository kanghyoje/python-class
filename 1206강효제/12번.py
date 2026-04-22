a = input()
li = []
for i in a:
  if i not in li:
    print(f"{i}{a.count(i)}",end='')
  li.append(i)