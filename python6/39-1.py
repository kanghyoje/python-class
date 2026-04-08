num = int(input("자연수 입력: "))
count = 0

for i in range(1, num + 1):
  count += i
print(f"1부터 {num}까지의 합은 {count}")