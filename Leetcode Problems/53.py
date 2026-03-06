"Given an array which contains each negative, positive, and zero values, we have to return the subarray with the maximum sum, and the maximum sum possible"
nums = [1]
# brute force solution/ better solution
# Time complexity : O(n2); space complexity : O(1)
# start,end = 0,0
# maximum = float('-inf')
# for i in range(len(nums)):
#     sum = 0
#     for j in range(i,len(nums)):
#         sum += nums[j]
#         if sum > maximum:
#             end = j
#             start = i
#             maximum = sum
# print(maximum,nums[start:end+1])

# optimal solution : Kadane's algorithm
'kadane algorithm says that when we need the maximum, there is no benefit of continuing with a negative sum,because it will ultimately even neturalize the positive, and wont have any good effect, so whenever we will encounter a negative sum, we will just reset the sum'
start = 0
end = 0
maximum, sum = 0, 0
for i in range(len(nums)):
    sum += nums[i]
    if sum < 0:
        sum = 0
        start = i+1
    elif sum > maximum:
        maximum = sum
        end = i
print(maximum,nums[start:end+1])