import functions
"""Arrays medium level questions"""
'Two sum : return the indices of two elements from the array which sums up to given target'
# nums  = [2,6,5,11,8]
# target = 14
# # brute force : Time complexity -> O(N^2)
# # space complexity : O(1)
# def sum2b(arr,target):
#     for i in range(len(arr)):
#         sum = arr[i]
#         for j in range(i+1,len(arr)):
#             if sum + arr[j] == target:
#                 return([i,j])
# # optimal solution : Hashing : time complexity : O(N^2 in worst case)
# # Space Complexity : O(N)
# def sum2opt(arr, target):
#     mp = {}
#     for i in range(len(arr)):
#         mp[arr[i]] = mp.get(arr[i],i)
#         check = target - arr[i]
#         if (check) in mp and mp[check] != i:
#             print(mp[check],i)
"sort array of 0's, 1's and 2's in place"
# nums = [0,1,2,0,1,2,1,2,0,0,0,1]
# brute force approach : sorting algorithms : N^2, or NlogN
# better approach : O(2N), space complexity : 0(1)
# def sortzotbe(arr:list)->None:
#     count0 = 0
#     count1 = 0
#     count2 = 0
#     for element in arr:
#         if element == 1:
#             count1 += 1
#         elif element  == 0:
#             count0 += 1
#         else :
#             count2 += 1
#     for j in range(count0):
#         arr[j] = 0
#     for j in range(count1):
#         arr[count0+j] = 1
#     for j in range(count2):
#         arr[count0 + count1+j] = 2
# sortzotbe(nums)

#optimal approach : Dutch National Flag Algorithm : 3 Pointer Method. Time complexity : 0(N), space complexity : O(1)
# nums = [0,1,2,0,1,2,1,2,0,0,0,1]
# def sortzotopt(arr:list):
#     left = 0
#     mid = 0
#     right = len(arr) - 1
#     while mid <= right:
#         if arr[mid] == 0:
#             temp = arr[left]
#             arr[left] = arr[mid]
#             arr[mid] = temp
#             mid += 1
#             left += 1
#         elif arr[mid] == 1:
#             mid += 1
#         elif arr[mid] == 2:
#             temp = arr[right]
#             arr[right] = arr[mid]
#             arr[mid] = temp
#             right -= 1
# sortzotopt(nums)
# print(nums)
"""majority element : return the element from the array which appears for more than n/2 times, where n is the length of the array."""
# brute force: O(n2) and space complexity of O(1)
# array = [2,2,3,3,1,2,2]
# minimum = len(array)//2
# for i in range(len(array)):
#     count = 1
#     element  = array[i]
#     for j in range(i+1,len(array)):
#         if array[j] == element:
#             count += 1
#         if count > minimum:
#             print(element)
#             break
# better approach : using hashing O(2N), space complexity of O(N)
# array = [1]
# minimum = len(array)//2
# mpp = {}
# for element in array:
#     mpp[element] = mpp.get(element,0)+1
# for key in mpp.keys():
#     if mpp[key] > minimum:
#         print(key)

# optimal solutions : Time complexity -> O(N) and space complexity -> O(1)

# array = [6,5,5]
# def moore_algo(nums):
#     count = 0
#     minimum = len(nums)//2
#     for i in range(len(nums)):
#         if count == 0:
#             element = nums[i]
#             count += 1
#         elif nums[i] == element:
#             count += 1
#         else:
#             count -= 1
#     x  = 0
#     for i in range(len(nums)):
#         if nums[i] == element:
#             x += 1
#     if x > minimum:
#         return(element)
#     return(-1)

# print(moore_algo(array))
"""Maximum subarray sum : Array contains positives, zeroes and negatives. Return the sum subarray having the highest sum"""
# better solution : using an n2 loop, if i were to use a n3 loop then it would have been extreme brute force, as there is no better solution if you were to consider n2 solution as the brute solution.
# nums = [5,4,-1,7,8]
# def maxsum_subarrb(nums):
#     max_sum = float('-inf')
#     for i in range(0,len(nums)):
#         sum = 0
#         for j in range(i,len(nums)):
#             sum += nums[j]
#             max_sum = max(sum,max_sum)
#     return max_sum
# Optimal solution :kadane's Algorithm O(N), and a space complexity of O(1)
# nums = [4, -6, 8, -5, 1, -7, 2, -5, 10, 1]
# sum = 0
# maximum = float('-inf')
# for i in range(len(nums)):
#     sum += nums[i]
#     maximum = max(sum,maximum)
#     if sum < 0: 
#         sum = 0
# print(maximum)
"""Print subarray with maximumm sum"""
# Optimal solution : Kadane's algorithm
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# maximum =  float('-inf')
# sum = 0
# start = 0
# end = 0
# for i in range(len(nums)):
#     sum += nums[i]
#     if sum < 0 :
#         sum = 0
#         start = i
#     if sum > maximum:
#         maximum = sum
#         end = i
# print(nums[start+1:end+1])
"""Best day to sell and buy stocks, and what is the maximum profit acheiveable. Where price of ith day is the ith index in the array"""
# prices =[7,1,5,3,6,4]
# 'brute force solution'

# profit = 0
# for i in range(len(prices)):
#     buy = i
#     for j in range(i+1,len(prices)):
#         profit = max(prices[j]-prices[buy],profit)
# print(profit)
# # time limit exceeded : Time complexity : O(n2), space complexity : O(1)

"optimal solution : Kadane's algorithm"
# buy = prices[0]
# profit = 0
# for i in range(1,len(prices)):
#     buy = min(buy,prices[i])
#     profit = max(profit,prices[i]-buy)
# print(profit)

"""Given an array, which contains negative, positive, and zeroes, you have to rearrange the array in place so that the negatives and positives are placed in the array alternatively, in the order of their initial placement."""
# brute force solution : Time complexity : O(2N); space complexity: O(N)
# nums = [3,1,-2,-5,2,-4]
# negs = []
# pos = []
# for num in nums:
#     if num >= 0:
#         pos.append(num)
#     else: 
#         negs.append(num)
# for i in range(len(pos)):
#     nums[2*i] = pos[i]
#     nums[2*i+1] = negs[i]
# print(nums)
# Optimal Solution: Time complexity: ; Space complexity: 
'Make an array with all the elements equal to zero and the number of elements will be equal to the length of the given array. Now take two pointers place one at zeroth index and the other add the first index. The pointer at the zeroth index will be named as positive and the pointer at the first index will be named as negative. Now we will iterate through the given array and if the element is positive then we will add it to the positive pointer index in the duplicate array and we will increase the positive pointer by two places and we will do the same for the negative At the end we will return the duplicate array.'

'---------------------------------------------------------------------------'
"""Next permutation. You are given an array nums, you have to return the next permutation of the array, without creating any space and returning the nums in place"""
# nums = [1,3,2]
# nums= [2,3,5,4,1,0,0]
# pivot = -1
# for i in range(len(nums)-1,0,-1):
#     if nums[i-1] < nums[i]:
#         pivot = i-1
#         break
# if pivot == -1:
#     nums.reverse()
# for i in range(len(nums)-1,pivot,-1):
#     if nums[i] > nums[pivot]:
#         temp = nums[i]
#         nums[i] = nums[pivot]
#         nums[pivot] = temp
#         start = pivot + 1
#         end = len(nums)-1
#         while start < end:
#             temp = nums[end]
#             nums[end] = nums[start]
#             nums[start] = temp
#             start += 1
#             end -= 1
# print(nums)
"""you are given an array, you have to return another array in which contains the leaders of the given array. An element in array is said to be leader, if all the elements appearing to the right of them are lesser than the element. The last element of the array is always the leader, as it is greater than all the elements appearing to the right of it"""
# nums = [10,22,12,3,7,0,6]
# nums = [5]
# nums = [3,3,3,3]
# nums= list(range(1,6))
# nums = [4,7,1,7]
# nums = [1,3,3,2]
# nums= [22,10,6]
# leaders = []
# brute force solution
# for i in range(len(nums)):
#     leader = nums[i]
#     while i < len(nums):
#         if nums[i] > leader:
#             break
#         i += 1
#     if i == len(nums):
#         leaders.append(leader)
# print(leaders)

# Optimal solution : Time complexity : O(N); Space complexity: O(k)
# maximum = float('-inf')
# for i in range(len(nums)-1,-1,-1):
#     if nums[i] >= maximum:
#         leaders.append(nums[i])
#         maximum = nums[i]
# print(leaders)

"""Given an array which will contains positive numbers, you have to return the longest sequence possible which contains all the consecutive numbers."""
# array = [102,4,101,100,2,1,3,1,1]
# brute force solution
# nums = [1,1,1,2,2,2,3,3,4,4,4]
# brute force solution
# longest = 1
# count = 1
# def find_element(arr:list,num:int):
#     for j in range(len(arr)):
#         if arr[j] == num:
#             return True
#     return False

# for i in range(len(array)):
#     element =  array[i]
#     count = 1
#     while(find_element(array,element+1) == True):
#         element += 1
#         count += 1
#         longest = max(count,longest)
# print(longest)

# better solution : Sorting
# nums= []
# nums.sort()
# count = 1
# last = float('-inf')
# longest = 0
# for i in range(len(nums)):
#     if last + 1 != nums[i]:
#         last = nums[i]
#         count = 1
#     elif last + 1 == nums[i]:
#         last = nums[i]
#         count += 1
#         longest = max(longest,count)
# print(longest)

# optimal solution
# nums = [102,4,101,100,2,1,3,1,1]
# longest = 1
# nums = set(nums)
# if len(nums) == 0: 
#     print(0)
# for i in range(len(nums)):
#     x = nums[i]
#     while x+1 in nums:
#         x += 1
#         count += 1
#         longest = max(count,longest)
# print(longest)