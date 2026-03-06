"""largest element in an array, without using the methods"""
# array_1 = [1,3,4,2,5,67,1,4,6]
# first = array_1[0]
# for i in range(len(array_1)):
#     if array_1[i] > first:
#         first =  array_1[i]
#     else:
#         pass
# print(first)
"""---------"""
# maximum =  max(array_1)
# print(maximum)
"""-------------"""
# array_1  = sorted(array_1)
# print(array_1[len(array_1) - 1])
"""Second largest element in an array without sorting"""
# array_1 = [1,3,4,2,5,67,67,1,4,6]
# largest =  array_1[0]
# second = array_1[0]
# for i in range(1,len(array_1)):
#     if array_1[i] > largest:
#         largest = array_1[i]
#     if  largest > array_1[i] > second :
#         second = array_1[i]
# print(largest, " || ", second)
"""---"""
# second = -1
# largest = array_1[0] 
# for i in range(1,len(array_1)):
#     if array_1[i] > largest : 
#         second = largest
#         largest = array_1[i]
#     elif array_1[i] > second and array_1[i] != largest:
#         second = array_1[i]
# print(second)
"""Check if array is sorted"""
# array_1 = [1,3,4,2,5,67,67,1,4,6]
# if sorted(array_1) == array_1 :
#     print("The array is sorted")
# else :
#     print("Not sorted")
"----"
# smallest = array_1[0]
# for i in range(1,len(array_1)):
#     if array_1[i] >= smallest:
#         smallest = array_1[i]
#     else:
#         print("NO")
#         exit()
"""Remove duplicates from sorted array"""
# a = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 7, 7, 7, 7]
# left =  0
# for i in range(0,len(a)):
#     if a[i] == a[left]:
#         pass
#     if a[i] != a[left]:
#         left += 1
#         a[left] = a[i]
# nums = nums[:k+1]
"""left rotate an array by one place"""
# brute force == best approach : time complexity O(N), space complexity = O(1), space used : O(N)
# nums = [3,5,1,5,4]
# temp = nums[0]
# for i in range(len(nums)-1):
#     nums[i] = nums[i+1]
# nums[-1] = temp
# print(nums)
'output'
# [5, 1, 5, 4, 3]

"""left rotate an array by `k` places"""
# nums = [1,2,3,4,5,6,7]
# d = 3
# n = len(nums)
# d = d%n

# def reverse(arr:list,i:int,j:int):
#     while i < j:
#         temp = arr[i]
#         arr[i] = arr[j]
#         arr[j] = temp 
#         i += 1
#         j -= 1
# def left_rotate(arr:list,d:int,leng:int) -> list:
    
#     reverse(arr,0,d-1)
#     reverse(arr,d,leng-1)
#     reverse(arr,0,leng-1)
# left_rotate(nums,d,n)
# print(nums)
"""take all zeroes to the end of array"""       
#brute force
# nums = [1,0,2,3,2,0,0,4,5,1]
# array = []
# counter = 0
# for num in nums:
#     if num == 0:
#         counter += 1
#     else:
#         array.append(num)
# for i in range(len(array)):
#     nums[i] = array[i]
# for i in range(len(array),len(nums)):
#     nums[i] = 0

#optimal
# nums = [1,0,2,3,2,0,0,4,5,1]
# j = nums.index(0)
# i = j+1
# while i < len(nums):
#     if nums[i] != 0:
#         nums[j] = nums[i]
#         nums[i] = 0
#         i += 1
#         j+= 1
#     elif nums[i] == 0:
#         i+= 1
# print(nums)

"""Linear Search"""
# nums = [25,12,8,4,6]
# def get_index(arr:list, number:int) -> int|bool:
#     for i in range(len(arr)):
#         if arr[i] == number:
#             return i
#     return f'{number} not found in {arr}'
# print(get_index([1,2,3,4],5))

"""Union of given two sorted arrays"""
from random import randint
# array,nums = [7, 9, 7, 10, 11, 13, 7, 7, 11, 6],[10, 7, 9, 10, 2, 1, 10, 9, 6, 7]
# brute force
# for num in nums:
#     array.append(num) # TC : O(M)
# array.sort()
# union = []
# for element in array:
#     if element in union:
#         continue
#     else:
#         union.append(element)
# print(union)

# optimal approach
# 2 pointer algorith
# array = [6, 7, 7, 7, 7, 9, 10, 11, 11, 13]
# nums = [1, 2, 6, 7, 7, 9, 9, 10, 10, 10]
# n1= len(array)
# n2 = len(nums)
# union = []
# i,j = 0,0
# while i<n1 and j<n2:
#     print(".")
#     if array[i] <= nums[j]:
#         if not union or union[-1] != array[i]:
#             union.append(array[i])
#         i += 1
#     elif array[i] > nums[j]:
#         if not union or union[-1] != nums[j]:
#             union.append(nums[j])
#         j += 1
# while i < n1:
#     if not union or union[-1] != array[i]:
#         union.append(array[i])
#     i += 1
# while j < n2:
#     if not union or union[-1] != nums[j]:
#         union.append(nums[j])
#     j += 1   
# print(union)

"""intersection of two arrays"""
# array = [6, 7, 7, 7, 7, 9, 10, 11, 11, 13]
# array2 = [1, 2, 6, 7, 7, 9, 9, 10, 10, 10]
# intersection = []
# vis = len(array2) *[0]
# for i in range(len(array)):
#     for j in range(i,len(array2)):
#         if array[i] == array2[j] and vis[j] == 0:
#             vis[j] += 1
#             intersection.append(array2[j])
#             break
#         elif array[i] < array2[j]:
#             break
#         else : continue
'optimal solution'
# n1 = len(array)
# n2 = len(array2)
# i = j = 0
# while i < n1 and j < n2:
#     if array[i] < array2[j]:
#         i += 1
#     elif array2[j] < array[i]:
#         j += 1
#     else :
#         intersection.append(array2[j])
#         i += 1
#         j += 1
# print(intersection)
"""Missing Number in an array"""
array = [0,2,3,4]
n = 4
# def missing_number(arr:list,max_int:int) -> int:
#     nums = list(range(1,max_int+1))
#     for element in nums:
#         if element not in arr:
#             return (element)
# print(missing_number(array,n))
# def better_missing_number(arr:list, max_int:int) -> int:
#     hash_Arr = (n+1)*[0]
#     for element in array:
#         hash_Arr[element] += 1
#     for i in range(1,len(hash_Arr)):
#         if hash_Arr[i] == 0:
#             return i
#     return 0
# print(better_missing_number(array,n))
# def opta_missing_number(arr:list, max_int:int) -> int:
#     expected = n*(n+1)//2
#     got  = sum(array)
#     return expected-got
# print(opta_missing_number(array, n))
"""Max consecutive ones"""
# ones = [1,1,0,0,0,1,1,1,0,1,1]
# def max_consecutive_1(arr:list) -> int:
#     maxi = 0
#     counter = 0 
#     for element in arr:
#         if element == 1:
#             counter += 1
#         if element == 0:
#             maxi = max(counter,maxi)
#             counter = 0
#     return(maxi)
# print(max_consecutive_1(ones))

"""return the element which appears once in array of each element appearing twice"""
#brute force
# nums = [1,1,2,2,-1,3,3,4,4]
# def element_once(arr:list):
#     mp = {}
#     for element in arr:
#         mp[element] = mp.get(element,0) + 1
#     for key in mp.keys():
#         if mp[key] == 1:
#             return key
# print(element_once(nums))
# def element_oncea(arr:list) -> int:
#     xor  = 0
#     for element in arr: 
#         xor ^=element
#     return xor
# print(element_oncea(nums))
"""longest subarray with sum equal to k"""
# nums = [1,2,3,1,1,1,4,2,3]
# l = 3
# long = 0
# for i in range(0,len(nums)):
#     for j in range(i,len(nums)):
#         sum = 0
#         for k in range(i,j):
#             sum += nums[k]
#         if sum == l:
#             long = max(long,j-i)
#         if sum > l:
#             break
# print(long)
"""longest subarray with sum equal to k; array only contains postives"""
# arr = [1,2,3,1,1,1,1,3,3]
# n = 3
#brute force
# def longest_subarr(arr:list, k:int) -> int|int:
#     count = 0
#     leng = 0
#     for i in range(len(arr)):
#         sum = 0
#         for j in range(i,len(arr)):
#             sum += arr[j]
#             if sum == k:
#                 count += 1
#                 leng = max(leng,j-i+1)
#     return count,leng

# print(longest_subarr(nums, k))

# better approach
# arr = [1,2,3,1,1,1,1,3,3]
# n = 3
# leng = 0
# sum = 0
# mp = {}
# for i in range(0,len(arr)):
#     sum += arr[i]
#     if sum == n:
#         leng = i+1
#     if sum not in mp:
#         mp[sum] = i
#     if (sum - n) in mp:
#         leng = max(leng,i-mp[sum-n])
# print(leng) 

# # best approach
# arr = [1,2,3,1,1,1,1,3,3]
# n = 3 
# sum = 0
# i = 0
# leng= 0
# while i < len(arr):
#     while sum <= n:
#         sum += arr[i]
#         if sum == n:
#             leng = max(leng,i + 1)
#         i += 1
#     j = 0
#     while sum > n:
#         sum -= arr[j]
#         j += 1
# print(leng)

