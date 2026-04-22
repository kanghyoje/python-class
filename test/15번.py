
for i in range(2, 10):
  print(f"[{i}단]")
  for j in range(1, 10):
    
    if (i * j) % 2 == 0:
      print(f"{i} x {j} = {i * j}")