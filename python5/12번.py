base = 270
use = int(input("전기 사용량(kW)입력:"))
if use > 100:
  cost = (use * base) * 1.2
else:
  cost = use * base
print("전기 사용량:", use, "kW")
print("전기 요금:", cost, "원")