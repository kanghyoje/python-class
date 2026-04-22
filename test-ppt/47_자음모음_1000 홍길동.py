a = input('영문자열 입력:')
a = a.lower()
con_c = 0
vow_c = 0
con = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'n', 'm', 'p', 'q' ,'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vow = ['a', 'e', 'i', 'o', 'u']
print("**********************")

for i in a:
  if i in vow:
    vow_c += 1
  elif i in con:
    con_c += 1
print(f"모음: {vow_c}개 자음: {con_c}개")