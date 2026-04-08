import random, time

w = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda', 'frog', 'snack', 'wolf']
n = 0
q = random.choice(w)
start = time.time()
count = 0

a = input("[타자게임] 준비되면 엔터")
while n < 5:
  count += 1
  print(f"[문제 {count}]")
  print(q)
  ans = input()
  if q == ans:
    n += 1
    print("pass")
  else:
    print("false")
  q = random.choice(w)

re = int(time.time() - start)
print(re)