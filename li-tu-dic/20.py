a = list(input().split())
len_dit = {}
for i in a:
  if len(i) not in len_dit:
    len_dit[len(i)] = []
  len_dit[len(i)].append(i)
print(len_dit)