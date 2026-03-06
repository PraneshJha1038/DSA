'number hashing/ array hashing'
import random
import time 
import math 
import string

'hashmap'
# numbers = [11, 8, 2, 0, 7, 0, 12, 12, 11, 10, 9, 4, 6, 4, 11, 11, 1, 7, 4, 10]
# fetch = dict.fromkeys((range(0,13)),0)
# for element in numbers:
#     fetch[element] += 1
# print(fetch)

'character hashing/ string hashing'

'hashmap'

characters = 'xylophonez'
# hashed = {}
# for char in characters:
#     hashed[char] = hashed.get(char,0) + 1
# print(hashed)


"""ASCII"""
'hash-array'

# array = 26*[0]

# random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(15))
# print(random_string)
# lower = ord('a')
# # create hash array
# for char in random_string:
#     array[ord(char)-lower] += 1


# # check hash array
# for element in array:
#     print(element, end="  ")
# for i in range(len(array)):
#     print(chr(i+ord('a')),end="  ")

'hashmap'
"""
when to use hash-maps(disctionaries):
Dictionary is used where there is no knowledge of what the input might be, or there is the need to store input only, and no pre-occupance is needed
-creates a O(1) complexity generally
"""
# random_string = 'vkqoulglpkvaqld'
# directory = {}
# for char in random_string:
#     directory[char] = directory.get(char,0)+1
