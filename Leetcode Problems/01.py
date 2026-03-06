'Two sum : return the indices of two elements from the array which sums up to given target'
# nums  = [2,6,5,11,8]
# target = 14
# brute force : Time complexity -> O(N^2)
# space complexity : O(1)
def sum2b(arr,target):
    for i in range(len(arr)):
        sum = arr[i]
        for j in range(i+1,len(arr)):
            if sum + arr[j] == target:
                return([i,j])
# better solution : Hashing : time complexity : O(N)
# Space Complexity : O(N)
def sum2be(arr:list, target:int):
    mp = {}
    for i in range(len(arr)):
        mp[arr[i]] = mp.get(arr[i],i)
        check = target - arr[i]
        if (check) in mp and mp[check] != i:
            print(mp[check],i)
sum2be([3,2,3],6)