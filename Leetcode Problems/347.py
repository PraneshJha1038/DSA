nums = [1,1,1,2,2,3,3,3,3,3,3]
k = 2
timer = max(nums)
freq = []
table = (timer+1)*[0]
for i in range(len(nums)):
    table[nums[i]] += 1
for i in range(k):
    timer = max(table)
    freq.append(table.index(timer))
    table[table.index(timer)] = 0
print(freq)