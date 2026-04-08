N = int(input())
nums = list(map(int, input().split()))

max_num = 0

for num in nums:
  reversed_num = int(str(num)[::-1])
  if reversed_num > max_num:
    max_num = reversed_num

print(max_num)