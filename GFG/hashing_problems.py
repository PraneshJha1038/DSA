# import random
"""confirm that there is no common element in both arrays"""
# a = [random.randint(1,8) for _ in range(70)]
# b = [random.randint(9,13) for _ in range(50)]
# for element in b:
#     if element in a:
#         print(False)
#         break
# print(True)
"""confirm if both arrays are equal"""
# a = [1,2,2,3,3]
# b = [2,2,1,3,8]
# mp = {}
# if len(a) != len(b):
#     print(False)
#     exit()
# for element in a:
#     mp[element] = mp.get(element,0) + 1
# for element in b:
#     if element not in mp:
#         print(False,end=",")
#         break
#     elif mp[element] == 0:
#         print(False)
#         break
#     mp[element] -= 1
# print(True)
"""Fizz Buzz"""
# def fizzBuzz(n):
#     list = []
#     for i in range(1,n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             list.append('FizzBuzz')
#         elif i % 5 == 0:
#             list.append('Buzz')
#         elif i % 3 == 0:
#             list.append('Fizz')
#         else:
#             list.append(i)
#     return(list)
# print(fizzBuzz(10))
"""maximum distance between two occurences"""
arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2,2]
mp = {}
res = 0

for i in range(len(arr)):
    if arr[i] not in mp:
        mp[arr[i]] = i
    else:
        res = max(res, i - mp[arr[i]])

print(res)