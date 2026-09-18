nums =  [3, 4, 6, 7, 9, 1, 2]
# Normally
def binarySearch(array):
    low = 0
    target = 6
    high = len(array) - 1
    while low <= high:
        mid = (low + high)//2
        if array[mid] > target:
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
        elif array[mid] == target:
            return(1>0)
        else:
            return(-1)
binarySearch(nums)

def binaryRecursionSearch(array:list[int],low:int,high:int,target:int)-> int:
    array.sort()
    if low > high:
        return -1
    mid = (low + high)//2
    if array[mid] > target: 
        return binaryRecursionSearch(nums,0,mid-1,target)
    elif array[mid] == target:
        return(mid)
    else:
        return binaryRecursionSearch(nums,mid+1,high,target)
'''
'Important: Overflow Case:'
'If the search space is such that the element float("inf") is the last index of the array, so (low+high)//2 will be again float("inf"), which overflows the algo'
'Therefore, low + (high-low)//2 can be used.'
'''
'lower Bound: It is the minimum value of index such that array[index] >= target'
arr = [3,5,6,7,8,13,16,18,19]
target = 8
def lowerBound(arr, target):
    high = len(arr)-1
    low = 0
    mini = len(arr)-1
    while high >= low:
        mid = (high + low)//2
        if arr[mid] >= target:
            high  = mid - 1
            mini = min(mini,mid)
        else:
            low = mid + 1
        return mini

# print(lowerBound(arr, target))
     
'upper bound: Upper bound is the minimum value of index of an array for which arr[index] > target'
arr = [3,5,6,7,8,13,16,18,19]
target = 8
def upperBound(array:list, num:int) -> int:
    mini = len(array)-1
    high = len(array)-1
    low = 0
    while high >= low:
        mid = (low + high)//2
        if array[mid] > num:
            high = mid - 1
            mini = min(mini,mid)
        else:
            low = mid + 1
    return mini
# print(upperBound(arr,target))

"Search Insert Position: You are given an array of distinct values, and a target value num. If num is present in the array, then return it's index, else return the index at which num should be inserted to mainitain the sorted order of the array"
array = [1,2,4,7]
target1 = 8
target2 = 3
answer1 = 2
answer2 = 2
def searchInsertPosition(arr:list, target:int) -> int:
    high = len(arr) -1
    low = 0
    result = len(arr)
    while high >= low:
        mid = (high + low)//2
        if arr[mid] >= target:
            high = mid - 1
            result = min(result,mid)
        else:
            low = mid + 1
    return result
# print(answer1 == searchInsertPosition(array, 4), "  ", answer2 == searchInsertPosition(array,target2))

"""First and last occurence of a given element"""
nums = [5,7,7,8,8,10]
k = 6
def firstOccurence(nums:list[int], k:int) -> int:
    low = 0
    high  = len(nums) - 1
    result = float('inf')
    while high >= low:
        mid = low + (high - low)//2
        if nums[mid] >= k:
            high = mid - 1
            result = min(mid,result)
        elif nums[mid] < k:
            low = mid + 1
    return result if type(result) == int else -1
# print(firstOccurence(nums, k))

def lastOccurence(nums:list[int], k:int) -> int:
    low = 0
    high  = len(nums) - 1
    result = float('-inf')
    while high >= low:
        mid = low + (high - low)//2
        if nums[mid] == k:
            low = mid + 1
            result = max(mid,result)
        elif nums[mid] < k:
            low = mid + 1
        elif nums[mid] > k:
            high = mid - 1
    return result if type(result) == int else -1
# print(lastOccurence(nums, k))

def firstAndLastOccurence(nums:list[int], k:int) -> list[int]:
    if firstOccurence(nums, k) == -1:
        return [-1,-1]
    return [firstOccurence(nums, k), lastOccurence(nums, k)]
print(firstAndLastOccurence(nums, k))

"""count number of occurences of a given element"""
# k = 4
# nums =  [1, 1, 2, 2, 2, 2, 2, 3]
# counter = 0
# if firstOccurence(nums, k) == -1:
#     print(counter)
# else:
#     i = firstOccurence(nums, k)
#     while nums[i] == k:
#         counter += 1
#         i += 1
#     print(counter)