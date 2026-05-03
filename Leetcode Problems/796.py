s = "abcde"
goal = "cdeab"
goal2 = "abced"
# approach 1
# def rotateString(s:str, goal:str):
#     chars = list()
#     for element in (s):
#         chars.append(element)
#     def leftRotate(arr):
#         temp = arr[0]
#         for i in range(len(arr)-1):
#             arr[i] = arr[i+1]
#         arr[-1] = temp
#     i = 0
#     while i < len(s):
#         leftRotate(chars)
#         if "".join(chars) == goal:
#             return(True)
#         i += 1
#     return(False)

# rotateString(s, goal)

def checkRotatedString(string:str, target:str) -> bool:
    return len(string) == len(goal) and goal in string + string
print(checkRotatedString(s,goal))
print(checkRotatedString(s,goal2))