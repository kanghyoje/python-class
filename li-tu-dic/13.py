name_li = list(input().split())
age_li = list(map(int, input().split()))
dic = {}

for i in range(len(name_li)):
  dic[name_li[i]] = age_li[i]

print(*dic.keys())
print(*dic.values())

