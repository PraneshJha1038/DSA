nums = [1,2,4]
k = 5
left = 0
right = 0
total = 0
max_freq = 0
nums.sort()
for right in range(len(nums)):
    total += nums[right]
    while nums[right]*(right-left+1) > total + k :
        total - nums[left]
        l += 1
    max_freq = max(max_freq,right-left+1)
print(max_freq)