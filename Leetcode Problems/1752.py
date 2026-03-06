import unittest
nums = [1,2,3]
def Test_sorted_rotated(arr:list)->bool:
    counter = 0
    for i in range(1,len(arr)):
        if arr[i-1] > arr[i]:
            counter += 1
    if nums[-1] > nums[0]:
        counter += 1

    return (counter <= 1)
print(Test_sorted_rotated(nums) == False)