files = input().split()
py = 0
txt = 0
jpg = 0

for file in files:
  if file[-3:] == ".py":    
    py += 1
  elif file[-4:] == ".txt": 
    txt += 1
  elif file[-4:] == ".jpg": 
    jpg += 1
print("py", py)
print("txt", txt)
print("jpg", jpg)