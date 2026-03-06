f"Sort Colors : Dutch National Flag Algorithm"
'You are given an array with three digits(colors), you have to sort the color in the order: [1,0,2]'
#brute force solution :
# nums = [2,0,2,1,1,0]
# zero = []
# one = []
# two = []
'-----'
# better solution : Time complexity : O(N) + O(N) -> O(2N); Space complexity : O(1)
# nums = [2,0,2,1,1,0]
# zero = 0
# one = 0
# two = 0
# for element in nums:
#     if element == 0:
#         zero += 1
#     elif element == 1:
#         one += 1
#     else:
#         two += 1
# for i in range(0,one):
#     nums[i] = 1
# for j in range(one,zero+one):
#     nums[j] = 0
# for k in range(zero+one,len(nums)):
#     nums[k] = 2
# print(nums)

#optimal solution : The Dutch National Flag Algorithm
'It is a three pointer method, lets say the pointers are low,mid and high. It assumes that all the element from 0 to low - 1 are equal to the first element to be placed. Further all the element from low to mid-1 are of the second element to be placed. Further, from mid to high - 1, all the elements are in unsorted order, and randomly placed. Finally all the elements from high to the end of array are of the last element to be placed.'
'The task is to just sort all the elements from mid<->high-1'
nums = [2,0,1]
low,mid = 0,0
high = len(nums)-1
while mid<=high:
    if nums[mid] == 1:
        temp = nums[mid]
        nums[mid] = nums[low]
        nums[low] = temp
        mid += 1
        low += 1 
    elif nums[mid] == 0:
        mid += 1
    else:
        temp = nums[high]
        nums[high] = nums[mid]
        nums[mid] = temp
        high -= 1
print(nums)