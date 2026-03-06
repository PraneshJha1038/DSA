import unittest
import time
count = 0
def recurrsion():
    global count
    if count ==  3:
        return
    print(count)
    count += 1
    recurrsion()

# recurrsion()
"""Print name 5 times using recurrsion"""
# count = 0
# def print_name(time,name):
#     """Add the number of time you want your name to be called
#     Also give your name as the second argument"""
#     global count
#     if count == time:
#         return
#     print(name)
#     count += 1
#     print_name(time=time,name=name)
# print_name(5,'pranesh')
"""print linearly from 1 to N"""
# def natural_numbers(start,end):
#     if start == end:
#         return
#     print(start)
#     natural_numbers(start+1,end=end)

# natural_numbers(39,89)
"""print linearly from N to 1"""
# def natural_numbers(start,end):
#     if start > end:
#         return
#     print(end)
#     natural_numbers(start,end-1)
# natural_numbers(3,10)
"""Print linealy from 1 to N by backtracking"""
# def back_tracking(n):
#     if (1 > n):
#         return
#     back_tracking(n-1)
#     print(n)
# back_tracking(5)
"""print sum of first n natural numbers"""
# # parametrised way

# def sum_n2(i,sum=0):
#     if (i<1):
#         print(sum)
#         return
#     sum_n2(i-1,sum+i)
# sum_n2(500)
"---"
# # functional way
# def sum_n(n):
#     if (n == 0):
#         return 0
#     return (n + sum_n(n-1))

# print(sum_n(500))

"""print n factorial by both paramatrised and functional way"""
# parametrised way
# def fac1(n,factorial=1):
#     if (n<1):
#         print(factorial)
#         return
#     fac1(n-1,factorial*n)
# fac1(5)
"---"
# functional way
# def fac2(n):
#     if (n == 1):
#         return 1
#     return n*fac2(n-1)
# print(fac2(5))

"""reverse and array using recursion"""
# parametric method
# array = [1,2,3,4,5,6]
# def revArr(l,r):
#     global array
#     if l < 0 or r >= len(array):
#         print("invalid indices: either l < 0 or r >= len(array)")
#         return
#     if l >= r:
#         print(array)
#         return
#     array[l],array[r] = array[r],array[l]
#     revArr(l+1,r-1)

# revArr(0,5) 

# functional method
nums = [1,2,3,7,4,5,6]
def revArr(array:list,i:int = 0):
    """
    :param i: i is the index from where you require to swap the array from
    """
    n = len(array)
    if i >= n/2:
        print(array)
        return 
    array[i],array[n-1-i] = array[n-i-1],array[i]
    revArr(array,i+1)
revArr(nums)
"""Check if a string is palindrome or not"""
# parametric recurrsion

# def check_palindrome_string(string:str,l,r):
#     """
#     Docstring for check_palindrome_string
    
#     :param string: String to be checked
#     :param l: 0th index of the string
#     :param r: nth index of the string
#     """
#     if (l >= r):
#          return True
#     elif string[l] != string[r]:
#         return False
#     if string[l] == string[r]:
#         check_palindrome_string(string,l+1,r-1)
#         return True

# def check_palindrome_string_func(string:str,i:int = 0):
#     n = len(string)
#     if (i > n//2):
#         return True
#     elif (string[i] != string[n-1-i]):
#         return False
#     return check_palindrome_string_func(string,i+1)
"""Fibonacci Number by recursion"""
# def fibonacci(n:int):
#     """Returns the Nth Fibonacci Number"""
#     if n <= 1:
#         return(n)
#     elif n == 1:
#         return(1)
#     return fibonacci(n-1) + fibonacci(n-2)
# for i in range(0,6):
#     print(f'{i}, {fibonacci(i)}')
# fibonacci = 0
# for i in range(5-1,0):
# n = 4
# if n <= 1:
#     print(n)
# else:
#     a,b = 0,1
#     for _ in range(1,n):
#         a,b = b, a + b 
#     print(b)
