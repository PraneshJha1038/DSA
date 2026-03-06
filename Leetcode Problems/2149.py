"""Given an array, which contains negative, positive, and zeroes, you have to rearrange the array in place so that the negatives and positives are placed in the array alternatively, in the order of their initial placement."""
# brute force solution : Time complexity : O(2N); space complexity: O(N)
nums = [3,1,-2,-5,2,-4]
negs = []
pos = []
for num in nums:
    if num >= 0:
        pos.append(num)
    else: 
        negs.append(num)
for i in range(len(pos)):
    nums[2*i] = pos[i]
    nums[2*i+1] = negs[i]

# Optimal Solution: 
