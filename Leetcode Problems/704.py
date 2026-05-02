nums , target = [-1,0,3,5,9,12], 9
def recu(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        elif nums[mid] == target:
            return(mid)
    return -1

print(recu(nums, target))