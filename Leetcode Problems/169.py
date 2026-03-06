'Given an array, with positive, negative and zero elements, you have to return the majority element. A majority element is an element which appears more than n/2 times in an array'
# brute force: Time complexity : O(n2); space complexity: O(1)
# array = [2,2,3,3,1,2,2]
# minimum = len(array)//2
# for i in range(len(array)):
#     element = array[i]
#     count = 0
#     for j in range(len(array)):
#         if array[j] == element:
#             count += 1
#     if count > minimum:
#         print(element)
#         break

# better solution @ hashing -> Time complexity : O(n) + O(N) : if array is decent (iykyk), else O(N+N2); space complexity: O(k), where k is the number of unique element in the array

# array = [2,2,3,3,1,2,2]
# minimum = len(array)//2
# mp = {}
# for element in array:
#     mp[element] = mp.get(element,0)+1
# for key in mp.keys():
#     if mp[key] > minimum:
#         print(key)

# optimal approach: MOORE'S VOTING ALGORITHM
'we will consider the first element of the array to be the majority element, if it is the majority element then it means that it appears for more than n//2 times, so if we were to take the number of times the element appears to be +1, and the number of time any other element appears to be -1, then the final count will never be 0, as it appears in the majority.'
"so if the element's count comes out to be 0 at any point, then it is not the majority element and we will consider the next element to be the majority element"
# array = [6,5,5]
# element = array[0]
# count = 1
# for i in range(1,len(array)):
#     if array[i] == element:
#         count += 1
#     else: 
#         count -= 1
#     if count == 0:
#         element = array[i]
#         count = 1
# print(element)
