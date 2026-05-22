nums = [4,5,6,7,0,1,2]
target = 0
## approach 1
def getIndex(nums, target):
    return(nums.index(target) if (target in nums) else -1)
