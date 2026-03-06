nums = [1,2,3,3,3,3,3,3,3,3,3,3]
hashmap = {}
for element in nums:
    if str(element) in hashmap.keys():
        print(element)
        break
    hashmap[str(element)] = hashmap.get(str(element),0) + 1