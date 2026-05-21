arr1, arr2 = [1,10,100], [1000]
arr1, arr2 = [1,2,3], [4,4,4]
maxLen = 0
i, j = 0, 0
hashSetA = set()
for element in arr1:
    while element:
        hashSetA.add(element)
        element = element // 10
for nums in arr2:
    while nums:
        if nums in hashSetA:
            maxLen = max(maxLen, len(str(nums)))
        nums = nums // 10
print(maxLen)