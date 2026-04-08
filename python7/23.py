nums = [1, 2, 2, 3, 3, 3]

for i in nums:
  if i > 0:
    if nums[i-1] == nums[i]:
      del nums[i-1]
print(tuple(nums))