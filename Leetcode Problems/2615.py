from collections import defaultdict
# brute force solution
nums:list[int] = [1,3,1,1,2]
# def hamming(nums):
#     mp = {}
#     arr = [0]*(len(nums))
#     for i in range(len(nums)):
#         if nums[i] not in mp:
#             mp[nums[i]] = [i]
#         else:
#             mp[nums[i]].append(i)
#     i = 0
#     for num in nums:
#         for element in mp[num]:
#             if element != i:
#                 arr[i] += abs(i-element)
#         i += 1
#     print(arr)
# hamming(nums)
n = len(nums)
groups = defaultdict(list)
for i, v in enumerate(nums):
    groups[v].append(i)
res = [0] * n
for group in groups.values():
    total = sum(group)
    prefix_total = 0
    sz = len(group)
    for i, idx in enumerate(group):
        res[idx] = total - prefix_total * 2 + idx * (2 * i - sz)
        prefix_total += idx
print(res)