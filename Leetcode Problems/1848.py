nums = [1,2,3,4,5]
target = 5
start = 3
distance = float('inf')
for i in range(len(nums)):
    if nums[i] == target:
        distance = min(distance, abs(start-i))
print(distance)