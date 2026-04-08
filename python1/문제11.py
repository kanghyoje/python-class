def list_avg(s_list) :
  sum = 0
  for i in s_list : # i에 score리스트의 숫자들을 넣는다.
    sum = sum + i # sum에 score리스트의 숫자들의 합을 대입한다.
  result = sum/len(s_list) # 평균 구한 값을 result변수에 대입한다.
  print('점수의 평균:', result) # 평균을 출력한다

score = [90, 80, 70, 50, 60]
list_avg(score) # 함수 호출 