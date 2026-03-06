import random
"""Selection Sorting
Take the minimum element to the left
time complexity : O(n^2)"""
# nums = [64, 25, 12, 22, 11]
# for i in range(len(nums)-1):
#     mini = i
#     for j in range(i,len(nums)):
#         if nums[mini] > nums[j]:
#             mini = j
#     temp = nums[mini]
#     nums[mini] = nums[i]
#     nums[i] = temp
'---------------------------------------------'
# for i in range(len(nums)-1):
#     mini = i
#     for j in range(i,len(nums)):
#         if nums[mini] > nums[j]:
#             mini = j
#     temp =  nums[mini]
#     nums[mini] =  nums[i]
#     nums[i] =  temp
# print(nums)

"""Bubble Sorting
Take the maximum element to the right
time complexity : O(n^2) : worst and average case
for the best case time complexity is O(n), and the best case is when the array is already sorted"""
nums = [64, 25, 12, 22, 11]

# for i in range(len(nums)-1):
#     counter = 0
#     for j in range(0,len(nums)-i-1):
#         if nums[j+1] < nums[j]:
#             temp = nums[j+1]
#             nums[j+1] = nums[j]
#             nums[j] = temp
#             counter = 1
#     if counter == 0 :
#         break
#     print('runs')
# print(nums)
'-----'
# for i in range(len(nums)-1):
#     counter = 0
#     for j in range(0,len(nums)-i-1):
#         if nums[j+1] < nums[j]:
#             temp = nums[j+1]
#             nums[j+1] = nums[j]
#             nums[j] = temp
#             counter = 1
#     if counter == 0:
#             break
# print(nums)

"""Insertion Sort
get an array, and correctly place all the elements to their place
"""
# nums = [64, 25, 12, 22, 11]
# for i in range(1,len(nums)): # 2
#     j = i
#     while j > 0 and nums[j-1] > nums[j]:
#         temp = nums[j]
#         nums[j] = nums[j-1]
#         nums[j-1] = temp
#         j -= 1
# print(nums)
