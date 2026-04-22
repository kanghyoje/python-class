while True:
  tu = tuple((input().split()))

  for i in range(len(tu)):
    if i == 0:
      continue
    if len(tu[i]) > len(tu[i-1]):
      max_len = tu[i]
  break
  
print(max_len)