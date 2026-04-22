str = input()

en = 0
nu = 0
sp = 0
es = 0
for i in str:
  if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
    en += 1

  elif '0' <= i <= '9':
    nu += 1

  elif i == " ":
    sp += 1

  else:
    es += 1
print(en, nu, sp, es)

  