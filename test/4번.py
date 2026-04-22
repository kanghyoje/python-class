word = input()

if word == word[::-1]:
  print("회문입니다.")
else:
  print("회문이 아닙니다.")