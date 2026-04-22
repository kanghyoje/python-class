password = input()
dic = {'alpha': 0, 'digit': 0, 'special':0}

for i in password:
  if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
    dic['alpha'] += 1

  elif '0' <= i <= '9':
    dic['digit'] += 1

  else:
    dic['special'] += 1
print(dic)
