nums = [1,1,2,2,3,3,4,5,6,6,6,6,7]
# 1
# left =  0
# for i in range(0,len(nums)):
#     if nums[i] != nums[left]:
#         left += 1
#         nums[left] = nums[i]
#     elif nums[i] == nums[left]:
#         continue
# k = left + 1
# print(nums)

# 2
l =0
for r in range(len(nums)-1):
    if nums[r + 1] == nums[l]:
        continue
    else :
        l += 1
        nums[l] = nums[r+1]
k = l
print(nums)