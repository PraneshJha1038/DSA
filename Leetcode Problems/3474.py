str1:str = "TFTF"
str2:str = "ab"

# def lexo(str1, str2):
#     n = len(str1)
#     m = len(str2)
#     word = ["a"] * (n + m - 1) 
#     fixed = [False] * (n + m - 1)
#     for i in range(len(str1)):
#         if str1[i] == "T":
#             j = i
#             while j <= i + m - 1:
#                 if not fixed[j]:
#                     word[j] = str2[j%m]
#                     fixed[j] = True
#                 if fixed[j] and str2[j%m] != word[j]:
#                     return ""
#                 j += 1
#         elif str1[i] == "F":
#             j = i
#             isEqual = True
#             while j <= i + m - 1:
#                 if word[j] != str2[j%m]:
#                     isEqual = False
#                     break
#             if isEqual:
#                 return ""
#         return "".join(word)

# print(lexo(first, second))

n = len(str1)
m = len(str2)

word = ["a"] * (n + m - 1)
fixed = [False] * (n + m - 1)

# Step 1: Handle all 'T'
for i in range(n):
    if str1[i] == "T":
        for j in range(m):
            pos = i + j
            if fixed[pos]:
                # already assigned → must match
                if word[pos] != str2[j]:
                    print("")
            else:
                word[pos] = str2[j]
                fixed[pos] = True

# Step 2: Handle all 'F'
for i in range(n):
    if str1[i] == "F":
        match = True
        for j in range(m):
            if word[i + j] != str2[j]:
                match = False
                break
        
        # If full match → need to break it
        if match:
            broken = False
            for j in range(m):
                pos = i + j
                
                # Try to modify only non-fixed positions
                if not fixed[pos]:
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c != str2[j]:
                            word[pos] = c
                            broken = True
                            break
                if broken:
                    break
            
            # If couldn't break → invalid
            if not broken:
                print("")

print("".join(word))