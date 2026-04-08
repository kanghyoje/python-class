data = ["A", "B", "A", "C", "B", "D", "A"]
data_li = []

for i in data:
  if i not in data_li:
    data_li.append(i)
print(data_li)