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
print(binaryRecursionSearch(nums,0,len(nums)-1,6))
'''
'Important: Overflow Case:'
'If the search space is such that the element float("inf") is the last index of the array, so (low+high)//2 will be again float("inf"), which overflows the algo'
'Therefore, low + (high-low)//2 can be used.'
'''