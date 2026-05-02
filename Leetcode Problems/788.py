# # # approach 1: manual checking O(nlogn)
# # def check(number:int) -> bool:
# #     changed = False
# #     while number != 0:
# #         last = (number%10)
# #         if last == 3 or last == 4 or last == 7:
# #             return False
# #         if last == 2 or last == 5 or last == 6 or last == 9:
# #             changed = True 
# #         number = number // 10
# #     return changed
# # count = 0
# # for i in range(1,n+1):
# #     if check(i):
# #         count += 1
# # return count

# # approach 2: recursion (n)
# # def solve(num:int) -> bool:
# #     if num == 0:
# #         return 0
# #     remaining = solve(num//10)
# #     d = num % 10
# #     check = 0
# #     if d == 0 or d == 1 or d == 8:
# #         check = 0
# #     elif d == 2 or d == 5 or d==6 or d ==9:
# #         check = 1 # good
# #     else:
# #         return 2 #invalid
# #     if (remaining == 0 and check == 0):
# #         return 0
# #     if (remaining == 2 or check == 2):
# #         return 2
# #     return 1
# # count = 0
# # for i in range(1,n+1):
# #     if solve(i) == 1:
# #         count += 1
# # return count 

# dp = [0] * (n + 1)
# count = 0

# for i in range(n + 1):
#     if i < 10:
#         if i in (0, 1, 8):
#             dp[i] = 1
#         elif i in (2, 5, 6, 9):
#             dp[i] = 2
#             count += 1
#         else:
#             dp[i] = 0
#     else:
#         a = dp[i // 10]
#         b = dp[i % 10]

#         if a == 1 and b == 1:
#             dp[i] = 1
#         elif a >= 1 and b >= 1:
#             dp[i] = 2
#             count += 1
#         else:
#             dp[i] = 0

# return count