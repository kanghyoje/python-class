nums = map(int, input().split())
nums_set = set()

for num in nums:
  nums_set.add(num)

nums_list = list(nums_set)
nums_list.sort()
print(nums_list)