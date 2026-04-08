seats = [("김민준", (1, 1)), ("이서연", (1, 2)), ("박지후", (1, 1)), ("최하은", (2, 1))]

dic = {}

seats = dict(seats) 

for name1, seat1 in seats.items():
  if seat1 not in dic:
    dic[seat1] = [name1]
  else:
    dic[seat1].append(name1)

print(dic)

for seat2, name2 in dic.items():
  if len(name2) == 2:
    print(seat2, name2)


 

    