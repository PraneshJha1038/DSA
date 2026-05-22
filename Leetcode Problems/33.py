nums = [4,5,6,7,0,1,2]
# [0,1,2]
target = 3
## approach 1
# def getIndex(nums, target):
#     return(nums.index(target) if (target in nums) else -1)
def modifiedBinary(nums, target):
    high = len(nums) - 1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            if nums[mid + 1] < nums[mid]:
                low = mid + 1
            else:
                high  = mid - 1
        elif nums[mid] < target:
            if nums[mid - 1] > nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        elif nums[mid] == target:
            return mid
    return -1
print(modifiedBinary(nums, target))