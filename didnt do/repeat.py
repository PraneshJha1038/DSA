nums = [1,2,3,1,1,1,4,2,3]
# brute force:
# for i in range(n):
#     sum = 0
#     for j in range(i,n):
#         sum += nums[j]
#         if sum == l:
#             longest = max(longest,j-i+1)
#         elif sum > l:
#             break
# print(longest)
'------------'
# better solution
# nums = [1,2,3,1,1,1,4,2,3]
# prefix_sum = []
# mp = {}
# k = 3
# longest = 0
# sum = 0
# for i in range(len(nums)):
#     sum += nums[i]
#     if sum == k:
#         longest = i+1
#     if sum not in mp:
#         mp[sum] = i
#     if sum-k in mp:
#         longest = max(longest,i-mp[sum-k])
# print(longest)
nums = [1,2,3,1,1,1,4,2,3]
j = 0
k = 3
sum = 0 
counter = 0
maximum = 0
for i in range(len(nums)):
    sum += nums[i]
    if sum <= k:
        counter += 1
        # maximum = max(counter,maximum)
    while sum > k:
        sum -= nums[j]
        j -= 1
        counter -= 1
print(counter)