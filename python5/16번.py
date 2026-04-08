point = input("점수를 입력하세요.")
point = int(point)
if point >= 90:
  print("성취도 A")
elif point >= 80:
  print("성취도 B")
elif point >= 70:
  print("성취도 C")
else:
  print("성취도 D")