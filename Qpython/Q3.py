data = [("김민준", "국어", 80), ("김민준", "영어", 90), ("이서연", "국어", 100), ("이서연", "영어", 95)]
result = {}

for i in data:
  if i[0] not in result:
    result[i[0]] = {i[1]:i[2]}
  else:
    result[i[0]][i[1]] = i[2]

kim_gook = result["김민준"]["국어"]
lee_gook = result["이서연"]["국어"] 
kim_eng = result["김민준"]["영어"]
lee_eng = result["이서연"]["영어"]
print(result)
print("김민준",sum(list(result["김민준"].values()))/ len(list(result["김민준"].values())))
print("이서연",sum(list(result["이서연"].values()))/ len(list(result["이서연"].values())))

print("국어", (kim_gook + lee_gook) / 2)
print("영어", (kim_eng + lee_eng) / 2)
