count = 0 
lenth = 0

while True: 
  score = int(input()) # 계속 

  if score == -1:
    
    break

  if score >= 0:
    continue
  else:
    print("잘못된 점수입니다.")
    continue
if count > 0:
  print(f"평균: {count / lenth}")
else:
  print("입력된 정수가 없습니다.")


   