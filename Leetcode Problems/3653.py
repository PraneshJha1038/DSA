nums = [1,1,1]
queries = [[0,2,1,4]]
for query in queries:
    for i in range(query[0], query[1] + 1, query[2]):
        nums[i] = (nums[i] * query[3]) % (10**9 + 7)
xor = 0
for num in nums: 
    xor ^= num
print(xor)