"""Longest subarray with sum k"""
"""Better solution : preSumMap and hashing"""
arr = [1,2,3,1,1,1,0,0,0,0,1,3,3]
preSumMap = {}
k = 3
curr = 0
maxi = 0
for i in range(len(arr)):
    curr += arr[i]
    if curr == k:
        maxi = max(maxi,i + 1)
    preSumMap[curr] = preSumMap.get(curr,i)
    if (curr - k) in preSumMap.keys():
        maxi = max(maxi, i - preSumMap[curr - k])
print(maxi)
