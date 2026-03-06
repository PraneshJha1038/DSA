import math
import time
"""Extraction of digits"""
# n = 7789
# digits = []
# counter = 0
# while n > 0:
#     counter += 1
#     last_digit = 7789 % 10
#     digits.append(last_digit)
#     n = int(n/10)
# print(f"The number of digits in 'n' is {counter}")
"---"
# n = 7789 
# print(f"The number of digits in given 'n' is {int(math.log10(n)+1)}")
"""reverse a number excluding the trailing zeroes"""
# n = 1234
# reversed_number = 0
# while n > 0:
#     last_digit = n % 10
#     reversed_number = reversed_number*10 + last_digit
#     n = int(n/10)
# print(reversed_number)
"""Check palindrome"""
# num = 12121
# num = str(num)
# print(num == (num)[::-1])
"---"
# n = 12344321
# reversed_n = 0
# new_n = n
# while new_n > 0 :
#     last_digit = new_n%10
#     reversed_n =  reversed_n*10 + last_digit
#     new_n = int(new_n/10)
# print(reversed_n == n)
"""Print all divisors in accending order"""
# n = 20
# expected = '1 2 4 5 10 20'
# # brute force : O(n)
# def divisors(n):
#     for i in range(1,n+1):
#         if (n % i == 0):
#             return (i)
#         else:
#             continue
# optimal solution

# root = int(math.sqrt(n))
# for i in range(1,root+1):
#     if (n % i == 0):
#         divisors.append(i)
#         if ((n//i)!=i):
#             divisors.append(n//i)
# divisors.sort()
# for divisor in divisors:
#     print(divisor,end=" ")
"""Check for prime"""
# n = 12
# counter = 0
# for i in range(1,int(11**(0.5))+1):
#     if ( n % i == 0):
#         counter += 1
#         if (n//i != i):
#             counter += 1
# if counter == 2:
#     print(True)
# else:
#     print(False)
# # time complexity : O(sqrtN)
# # space complexity :  O(1)
"""GCD"""
# n1 = 21
# n2 = 14
# for i in range(min(n1,n2),0,-1):
#     if ((n1 % i == 0) and (n2 % i == 0)):
#         gcd = i
#         break
# print(gcd)
"---"
# a = 21
# b = 14
# while a > 0 and b > 0:
#     if a > b: 
#         a = a % b
#     else :
#         b = b % a
# if a == 0:
#     print(b)
# else:
#     print(a)

