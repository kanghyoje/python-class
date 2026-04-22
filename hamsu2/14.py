s = 0
def f(n):
  global s
  k = 0
  while k < n:
    k = k + 1
    s = s + k

  
  f(3)
  print(s)