nums = list(map(int,input().split()))
N = int(input())

for i in range(N):
  nums.insert(0,nums[-1])
  del nums[-1]
print(nums)