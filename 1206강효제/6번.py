password = input()
alpha = 0
num = 0
for ch in password:
  if ch.isalpha():
    alpha += 1
  if ch.isdigit():
    num += 1

if len(password) >= 8 and alpha >= 1 and num >= 1: 
  print("사용 가능")
else:
  print("사용 불가")