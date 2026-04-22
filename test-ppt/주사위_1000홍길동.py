for a in range(1, 7):
  for b in range(1, 7):
    print(f"({a}, {b})", end=' ')
  print()

for e in range(1,7):
  for f in range(1,7):
    print(f"({f}, {e})",end=' ')
  print()

for c in range(1, 7):
  for d in range(1, 7):
    if c != d:
      print(f"({c}, {d})", end=' ')
    else:
      print("       ", end='')
      
  print()