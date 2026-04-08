students = [
  [101, "김민준", "로봇"],
  [102, "이서연", "방송"],
  [103, "박지후", "로봇"],
  [104, "최하은", "도서"]
]
target_id = 103
result = {}
result_1 = {}
for i in students:
  result[i[0]] = [i[1], i[2]]
  if i[2] not in result_1:
    result_1[i[2]] = 1
  else:
    result_1[i[2]] += 1
print(result)
print(result[target_id][0], result[target_id][1])
print(result_1)

  