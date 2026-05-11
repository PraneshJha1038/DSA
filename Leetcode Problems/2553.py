# approach 1: elongated version
def hi():
    def returnDigits(num:int) -> str|None:
        string = ""
        while num != 0:
            last = num % 10
            string = string + str(last)
            num = num // 10
        return string[::-1]
    def returnCombinedDigits(arr:list) -> list|None:
        string = ""
        final = list()
        for num in arr:
            string = string + str(returnDigits(num))
        for chr in str(string):
            final.append(int(chr))
        return final
    return(returnCombinedDigits([13,11,14,15,12]))

print(hi())
# approach 2
result  = list()
nums =  [13,11,14,15,12]
for num in nums:
    s = str(nums)
    for char in s:
        result.append(char)
    print(result)