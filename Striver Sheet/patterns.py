# https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa
"""1"""
# for i in range(5):
#     print('*'*5)

"""2"""
# for i in range(1,6):
#     print("*"*i)

"""3"""
# rows = 4
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()
"""4"""
# for i in range(1,6):
#     for j in range(0,i):
#         print(i,end="")
#     print()
"""5"""
# for i in range(1,6)[::-1]:
#     print("*"*i)
# for i in range(-5,0):
#     print("*"*(i*-1))
# for i in range(5,0,-1):
#     print("*"*i)
"""6"""
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
"""7"""
# n = 4
# for i in range(0,n):
#     print(' '*(n-i),'*'*(2*i+1))
"""8"""
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
"""9"""
# n = 4
# for i in range(0,n+1):
#     print("*"*i)
# for i in range(0,n+1)[::-1]:
#     print("*"*i)
"""10"""
# for i in range(1,6):
#     for j in range(0,i):
#         print(1-(j%2),end="")
#     print()

"""11"""
# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print(" "*(2*(n-i)),end="")
#     for j in range(1,i+1)[::-1]:
#         print(j,end="")
#     print()
    
"""12"""
# current = 1 
# rows = 10
# for i in range(1,rows + 1):
#     for j in range(current, current + i):
#         print(j,end=" ")
#     current += i
#     print()
"""13"""
regional_indicator = ["A", "B", "C", "D", "E"]
# for i in range(1,6):
#     for j in range(0,i):
#         print(regional_indicator[j],end="")
#     print()
"""14"""
# for i in range(1,6)[::-1]:
#     for j in range(0,i):
#         print(regional_indicator[j],end="")
#     print()
"""15"""
# for i in range(0,5):
#     print(regional_indicator[i]*(i+1))
"""16"""
# rows = 5
# for i in range(1,rows+1):
#     print(" "*(rows-i),end="")
#     for j in range(0,i):
#         print(regional_indicator[j],end="")
#     for j in range(0,i-1)[::-1]:
#         print(regional_indicator[j],end="")
#     print()
"""17"""
# for i in range(0,5):
#     for j in range(4-i,5)[::-1]:
#         print(regional_indicator[j],end=" ")
#     print()
"""18"""

# n = 4
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print(' '*(2*(n-i)),end="")
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print(" "*(2*(n-i)),end="")
#     for j in range(1,i+1)[::-1]:
#         print(j,end="")
#     print()
